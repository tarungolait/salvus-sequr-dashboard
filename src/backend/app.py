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

if __name__ == '__main__':
    app.run(debug=True)
