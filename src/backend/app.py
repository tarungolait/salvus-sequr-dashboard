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
                postgres_insert_query = """INSERT INTO data_entry (barcodeno, wallet_type, walletcolor, manufacturingdate, batchnum, countrycode, qrcode, blemacid, version, barcode_location, qrcode_location) 
                                   VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""  # Updated query to include barcode_location and qrcode_location
                record_to_insert = (
                    data['barcodeno'],
                    data['wallet_type'],
                    data['walletcolor'],
                    data['manufacturingdate'],
                    data['batchnum'],
                    data['countrycode'],
                    data['qrcode'],
                    data['blemacid'],
                    data['version'],
                    None,  # Placeholder for barcode_location
                    None   # Placeholder for qrcode_location
                )
                cursor.execute(postgres_insert_query, record_to_insert)
                connection.commit()
                count_records = cursor.rowcount

        qrcode_url, barcode_url = generate_codes(data['qrcode'], data['barcodeno'], data['version'], data['wallet_type'], data['blemacid'])

        # Update the database with barcode and qrcode locations
        with psycopg2.connect(**db_config) as connection:
            with connection.cursor() as cursor:
                update_query = """UPDATE data_entry SET barcode_location = %s, qrcode_location = %s WHERE barcodeno = %s"""
                cursor.execute(update_query, (barcode_url, qrcode_url, data['barcodeno']))
                connection.commit()

        return jsonify({'message': f'{count_records} Record(s) inserted successfully', 'qrcode_url': qrcode_url, 'barcode_url': barcode_url})

    except Exception as error:
        return jsonify({'error': str(error)})

def generate_codes(qrcode_data, barcode_data, version, wallet_type, blemacid):
    encrypted_data = encrypt_data(qrcode_data, barcode_data, version, wallet_type, blemacid)
    qrcode_url = generate_qrcode(encrypted_data, barcode_data)
    barcode_url = generate_barcode(barcode_data, barcode_data)
    return qrcode_url, barcode_url

def encrypt_data(qrcode, blemacid, barcodeno, version, wallet_type):
    site = [qrcode, ',', blemacid, ',', barcodeno, ',', version, ',', wallet_type,
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
    return f"http://127.0.0.1:5500/src/backend/BAR_QR_FOLDER/{qr_code_filename}"

def generate_barcode(barcode_data, filename):
    my_code = EAN13(barcode_data, writer=SVGWriter())
    barcode_filename = f"{filename}_barcode"
    barcode_path = os.path.join(BAR_QR_FOLDER, barcode_filename)
    my_code.save(barcode_path)
    return f"http://127.0.0.1:5500/src/backend/BAR_QR_FOLDER/{barcode_filename}.svg"

if __name__ == '__main__':
    app.run(debug=True)
