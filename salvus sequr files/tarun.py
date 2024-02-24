from flask import Flask, jsonify, request
from flask_cors import CORS
import psycopg2
import sys

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing (CORS)

# PostgreSQL database connection
try:
    mydb = psycopg2.connect(
        host="localhost",
        port=5432,
        database="infinicue",
        user="postgres",
        password="zaynmalik2002"
    )
except psycopg2.Error as e:
    print('Unable to connect with database due to ', e)
    sys.exit()

# Endpoint to handle POST request
@app.route('/userdetail', methods=['POST'])
def user_post():
    # Get JSON data from request
    data = request.get_json()

    # Extract relevant fields from JSON data
    barcodeno = data.get('barcodeno')
    product = data.get('Product')
    device_id = data.get('device_id')
    name = data.get('Name')
    phone = data.get('phone')
    email = data.get('Email')
    qrcode = data.get('qrcode')  # Added qrcode extraction

    # Check if there is existing data in the database based on barcodeno and product
    with mydb.cursor() as cursor:
        cursor.execute('SELECT * FROM infinicue_master_table WHERE barcodeno = %s AND product = %s', (barcodeno, product))
        existing_data = cursor.fetchone()

    if existing_data:
        # Data exists in the database
        return jsonify({'message': 'Successful'}), 200
    else:
        # Data does not exist in the database, insert into devicedata and userdata tables
        with mydb.cursor() as cursor:
            cursor.execute("INSERT INTO devicedata (device_id, barcodeno, qrcode) VALUES (%s, %s, %s)", (device_id, barcodeno, qrcode))
            cursor.execute("INSERT INTO userdata (name, phone, email, barcodeno, qrcode) VALUES (%s, %s, %s, %s, %s)", (name, phone, email, barcodeno, qrcode))
            mydb.commit()

        return jsonify({'message': 'Data inserted successfully'}), 201

# Run Flask app
if __name__ == '__main__':
    app.run(debug=True)
