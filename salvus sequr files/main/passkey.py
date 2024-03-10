from flask import Flask, jsonify, request
from flask_cors import CORS
import psycopg2
import random
import sys

app = Flask(__name__)
CORS(app)

# Database connection
try:
    connection = psycopg2.connect(
        host="localhost",
        port=5432,
        database="infinicue",
        user="postgres",
        password="zaynmalik2002"
    )
except psycopg2.Error as e:
    print('Unable to connect with database due to:', e)
    sys.exit()

# API endpoint to insert data into 'devicedata' and 'userdata' tables
@app.route('/insert_data', methods=['POST'])
def insert_data():
    try:
        data = request.get_json()
        cursor = connection.cursor()

        # Insert data into 'devicedata' table
        cursor.execute("INSERT INTO devicedata (device_id, barcodeno, qrcode) VALUES (%s, %s, %s)",
                       (data['device_id'], data['barcodeno'], data['qrcode']))

        # Insert data into 'userdata' table
        cursor.execute("INSERT INTO userdata (name, last_name, phone, email, barcodeno, qrcode) VALUES (%s, %s, %s, %s, %s, %s)",
                       (data['name'], data['last_name'], data['phone'], data['email'], data['barcodeno'], data['qrcode']))

        connection.commit()
        cursor.close()

        # Retrieve data from 'devicedata' and 'userdata' tables
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM devicedata WHERE qrcode = %s", (data['qrcode'],))
        devicedata_rows = cursor.fetchall()

        cursor.execute("SELECT * FROM userdata WHERE qrcode = %s", (data['qrcode'],))
        userdata_rows = cursor.fetchall()

        cursor.close()

        # Combine relevant fields from both tables to generate passkey
        combined_fields = ''
        fields = ['name', 'last_name', 'phone', 'device_id', 'qrcode', 'barcodeno']
        for field in fields:
            # Selecting one character randomly from each field
            combined_fields += random.choice(devicedata_rows[0]) if 'device' in field else random.choice(userdata_rows[0])

        # Generate a 7-character long passkey
        passkey = ''.join(random.sample(combined_fields, 7))

        return jsonify({'passkey': passkey}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
