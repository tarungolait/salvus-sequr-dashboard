from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import psycopg2
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from pyqrcode import create as pyqrcode_create
from barcode import EAN13
from barcode.writer import SVGWriter

app = Flask(__name__)
CORS(app)

# Database connection configuration
db_config = {
    'user': 'postgres',
    'password': 'zaynmalik2002',
    'host': 'localhost',
    'port': '5432',
    'database': 'infinicue',
}

BAR_QR_FOLDER = 'src/backend/BAR_QR_FOLDER'

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', 'http://localhost:3000')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

@app.route('/api/product-codes', methods=['GET'])
def get_product_codes():
    try:
        increment_on_submit = request.args.get('increment_on_submit') == 'true'

        with psycopg2.connect(**db_config) as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT id, qrcode, barcodeno FROM ProductCodes ORDER BY id DESC LIMIT 1")
                last_product_code = cursor.fetchone()

                if last_product_code:
                    last_qrcode = last_product_code[1]
                    last_barcodeno = last_product_code[2]
                else:
                    # If no records exist, start with initial values
                    last_qrcode = "00000"
                    last_barcodeno = "890202400000"

                if increment_on_submit:
                    # Increment the last values for the next record
                    next_qrcode = str(int(last_qrcode) + 1).zfill(len(last_qrcode))
                    next_barcodeno = str(int(last_barcodeno) + 1)
                else:
                    # Return the current values without incrementing
                    next_qrcode = last_qrcode
                    next_barcodeno = last_barcodeno

                # Insert the new record with the incremented values
                if increment_on_submit:
                    cursor.execute("INSERT INTO ProductCodes (qrcode, barcodeno) VALUES (%s, %s) RETURNING id", (next_qrcode, next_barcodeno))
                    new_id = cursor.fetchone()[0]
                    connection.commit()
                else:
                    new_id = None

        return jsonify({
            'id': new_id,
            'qrCode': next_qrcode,
            'barcodeNo': next_barcodeno
        })

    except Exception as error:
        return jsonify({'error': str(error)})



    
@app.route('/api/product-details', methods=['POST'])
def add_product_details():
    try:
        data = request.json
        with psycopg2.connect(**db_config) as connection:
            with connection.cursor() as cursor:
                postgres_insert_query = """INSERT INTO product_details (product_category, product_type, color, battery_type, ble_make, version) 
                                   VALUES (%s, %s, %s, %s, %s, %s)"""
                record_to_insert = (
                    data['product_category'],
                    data['product_type'],
                    data['color'],
                    data['battery_type'],
                    data['ble_make'],
                    data['version']
                )
                cursor.execute(postgres_insert_query, record_to_insert)
                connection.commit()
                count_records = cursor.rowcount

        return jsonify({'message': f'{count_records} Record(s) inserted successfully'})

    except Exception as error:
        return jsonify({'error': str(error)})
    
@app.route('/api/product-details', methods=['GET'])
def get_product_details():
    try:
        with psycopg2.connect(**db_config) as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT DISTINCT product_category FROM product_details")
                categories = [row[0] for row in cursor.fetchall()]

                cursor.execute("SELECT DISTINCT product_type FROM product_details")
                types = [row[0] for row in cursor.fetchall()]

                cursor.execute("SELECT DISTINCT color FROM product_details")
                colors = [row[0] for row in cursor.fetchall()]

                cursor.execute("SELECT DISTINCT version FROM product_details")
                versions = [row[0] for row in cursor.fetchall()]

        return jsonify({
            'categories': categories,
            'types': types,
            'colors': colors,
            'versions': versions
        })

    except Exception as error:
        return jsonify({'error': str(error)})

@app.route('/api/data-entry', methods=['POST'])
def add_data_entry():
    try:
        data = request.json
        with psycopg2.connect(**db_config) as connection:
            with connection.cursor() as cursor:
                postgres_insert_query = """INSERT INTO data_entry (category, type, color, macId, qrCode, barcodeNo, version, batchNumber, countryCode, manufacturingDate, barcode_location, qrcode_location) 
                                   VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""  # Updated query to match the frontend form fields
                record_to_insert = (
                    data['category'],
                    data['type'],
                    data['color'],
                    data['macId'],
                    data['qrCode'],
                    data['barcodeNo'],
                    data['version'],
                    data['batchNumber'],
                    data['countryCode'],
                    data['manufacturingDate'],
                    None,  # Placeholder for barcode_location
                    None   # Placeholder for qrcode_location
                )
                cursor.execute(postgres_insert_query, record_to_insert)
                connection.commit()
                count_records = cursor.rowcount

        encrypted_data = encrypt_data(data['qrCode'], data['macId'], data['barcodeNo'], data['version'], data['type'])
        qrcode_url, barcode_url = generate_codes(encrypted_data, data['barcodeNo'], data['version'], data['type'], data['macId'])

        # Update the database with barcode and qrcode locations
        with psycopg2.connect(**db_config) as connection:
            with connection.cursor() as cursor:
                update_query = """UPDATE data_entry SET barcode_location = %s, qrcode_location = %s WHERE barcodeNo = %s"""
                cursor.execute(update_query, (barcode_url, qrcode_url, data['barcodeNo']))
                connection.commit()

        return jsonify({'message': f'{count_records} Record(s) inserted successfully', 'qrcode_url': qrcode_url, 'barcode_url': barcode_url})

    except Exception as error:
        return jsonify({'error': str(error)})

def generate_codes(qrcode_data, barcode_data, version, item_type, mac_id):
    qrcode_url = generate_qrcode(qrcode_data, barcode_data)
    barcode_url = generate_barcode(barcode_data)
    return qrcode_url, barcode_url

def encrypt_data(qrcode, mac_id, barcode_no, version, wallet_type):
    site = [qrcode, ',', mac_id, ',', barcode_no, ',', version, ',', wallet_type,
            ',\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10']
    str_qr = ''.join(site)
    qr_byte = str_qr.encode('utf-8')

    key = 'helloworldhelloo'.encode('utf-8')
    iv = 'helloworldhelloo'.encode('utf-8')
    aes = AES.new(key, AES.MODE_CBC, iv)

    encrypted_data = aes.encrypt(pad(qr_byte, AES.block_size))
    encoded_data = base64.b64encode(encrypted_data).decode('utf-8')

    return encoded_data

def generate_qrcode(qr_data, filename, scale_factor=5):
    qr_code = pyqrcode_create(qr_data)
    qr_code_filename = f"{filename}_qrcode.svg"
    qr_code_path = os.path.join(BAR_QR_FOLDER, qr_code_filename)
    qr_code.svg(qr_code_path, scale=scale_factor)
    return f"http://127.0.0.1:5500/src/backend/BAR_QR_FOLDER/{qr_code_filename}?data={qr_data}"

def generate_barcode(barcode_data):
    my_code = EAN13(barcode_data, writer=SVGWriter())
    barcode_filename = f"{barcode_data}_barcode"
    barcode_path = os.path.join(BAR_QR_FOLDER, barcode_filename)
    my_code.save(barcode_path)
    return f"http://127.0.0.1:5500/src/backend/BAR_QR_FOLDER/{barcode_filename}.svg"

@app.route('/api/bankcontacts', methods=['POST'])
def add_bank_contact():
    try:
        data = request.json
        with psycopg2.connect(**db_config) as connection:
            with connection.cursor() as cursor:
                postgres_insert_query = """INSERT INTO bank_contacts (bank_name, type_of_bank, address, city, country, customer_care_number, email_id, official_website) 
                                   VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
                record_to_insert = (
                    data['bankName'],
                    data['typeOfBank'],
                    data['address'],
                    data['city'],
                    data['country'],
                    data['customerCareNumber'],
                    data['emailId'],
                    data['officialWebsite']
                )
                cursor.execute(postgres_insert_query, record_to_insert)
                connection.commit()
                count_records = cursor.rowcount

        return jsonify({'message': f'{count_records} Record(s) inserted successfully'})

    except Exception as error:
        return jsonify({'error': str(error)})


if __name__ == '__main__':
    app.run(debug=True)
