from flask import Flask, jsonify, request
from flask_cors import CORS
from Crypto.Cipher import AES
import base64
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

# Connect to the database
def connect_to_database():
    return psycopg2.connect(
        host="localhost",
        port=5432,
        database="infinicue",
        user="postgres",
        password="zaynmalik2002"
    )

# Route for decrypting and extracting data from the encrypted QR code
@app.route('/decrypt', methods=['POST'])
def decrypt_qr_code():
    # Get encrypted data from request
    encrypted_data = request.json.get('encrypted_data')

    # Decrypt and extract data
    try:
        # Initialize AES cipher with the same key and IV used for encryption
        key = 'helloworldhelloo'.encode('utf-8')  # Same key as encryption
        iv = 'helloworldhelloo'.encode('utf-8')   # Same IV as encryption
        aes = AES.new(key, AES.MODE_CBC, iv)

        # Decode the base64 encoded string
        encrypted_data_bytes = base64.b64decode(encrypted_data)

        # Decrypt the data
        decrypted_data = aes.decrypt(encrypted_data_bytes)

        # Decode the decrypted bytes to get the original string
        decoded_data = decrypted_data.decode('utf-8')

        # Split the decrypted string to extract individual fields
        decoded_fields = decoded_data.split(',')

        # Extracting individual fields
        qrcode = decoded_fields[0]
        blemacid = decoded_fields[1]
        barcodeno = decoded_fields[2]
        version = decoded_fields[3]
        ty = decoded_fields[4]

        # Connect to the database
        conn = connect_to_database()
        cursor = conn.cursor()

        # Check if barcode exists in any of the tables
        cursor.execute("SELECT barcodeno FROM infinicue_master_table WHERE barcodeno = %s", (barcodeno,))
        if cursor.fetchone():
            conn.close()
            return jsonify({'message': 'successful'}), 200

        cursor.execute("SELECT barcodeno FROM barcode WHERE barcodeno = %s", (barcodeno,))
        if cursor.fetchone():
            conn.close()
            return jsonify({'message': 'successful'}), 200

        cursor.execute("SELECT barcodeno FROM qrcode WHERE barcodeno = %s", (barcodeno,))
        if cursor.fetchone():
            conn.close()
            return jsonify({'message': 'successful'}), 200

        cursor.execute("SELECT barcodeno FROM retailer_user WHERE barcodeno = %s", (barcodeno,))
        if cursor.fetchone():
            conn.close()
            return jsonify({'message': 'successful'}), 200

        conn.close()
        return jsonify({'message': 'unsuccessful'}), 404

    except Exception as e:
        return jsonify({'error': str(e)}), 400

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
