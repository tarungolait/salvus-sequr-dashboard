from flask import Flask, jsonify, request
from flask_cors import CORS
from Crypto.Cipher import AES
import psycopg2
import base64
import sys

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing (CORS)

# Attempt to connect to PostgreSQL database
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

# Configure Flask app settings
app.config['SECRET_KEY'] = 'Infinicue'  # Set secret key for Flask app
app.config['SESSION_COOKIE_SECURE'] = True  # Set session cookie to be secure

# Function to handle QR code data
@app.route('/')
def index():
    return 'Connected'

@app.route('/post', methods=['GET', 'POST'])
def qr_code():
    if request.method == 'POST':
        df2 = request.get_json(force=True)
        df1 = df2['QRcode']
        ff = base64.b64decode(df1)
        key = 'helloworldhelloo'.encode('utf-8')
        text = 'helloworldhello'.encode('utf-8')
        iv = 'helloworldhelloo'.encode('utf-8')
        aes = AES.new(key, AES.MODE_CBC, iv)
        en = aes.decrypt(ff)
        en_str = en.decode('utf-8')
        QR_code = en_str.split(',')
        barcode_no = QR_code[2]
        version = QR_code[3]
        ble_mac_id = QR_code[1]
        qr_code = QR_code[0]
        device_idd = QR_code[5]
        product = QR_code[4]
        mycursor = mydb.cursor()
        mycursor.execute("ROLLBACK")
        mydb.commit()
        mycursor.execute('SELECT qrcode, device_id FROM infinicue_master_table WHERE qrcode=%s AND product=%s', [qr_code, product])
        existed_data = mycursor.fetchone()
        if not existed_data:
            mycursor.execute('SELECT barcodeno FROM barcode WHERE barcodeno=%s', [barcode_no])
            bar = mycursor.fetchone()
            if not bar:
                return jsonify({"message": "unsuccessful"})
            else:
                mycursor.execute('SELECT barcodeno FROM qrcode WHERE barcodeno=%s', [barcode_no])
                barcodeno_qr = mycursor.fetchone()
                if not barcodeno_qr:
                    return jsonify({"message": "unsuccessful"})
                else:
                    mycursor.execute('SELECT name, email, phone FROM retailer_user WHERE barcodeno = %s', [barcode_no])
                    res = mycursor.fetchone()
                    if not res:
                        return jsonify({'message': 'successful'})
                    else:
                        return jsonify({'name': res[0], 'email': res[1], 'phone': res[2], 'message': 'successful'})
        else:
            if existed_data[1] == device_idd:
                mycursor.execute('SELECT name, email, phone FROM retailer_user WHERE barcodeno = %s', [barcode_no])
                res = mycursor.fetchone()
                if not res:
                    return jsonify({'message': 'successful'})
                else:
                    return jsonify({'name': res[0], 'email': res[1], 'phone': res[2], 'message': 'successful'})
            else:
                return jsonify({'message': 'successful'})

# Route to handle API call for updating QR code data with additional information
@app.route('/update_qr_data', methods=['POST'])
def update_qr_data():
    if request.method == 'POST':
        data = request.get_json(force=True)
        
        # Extracting data from the JSON payload
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data.get('email')
        phone_number = data.get('phone_number')
        device_id = data.get('device_id')
        device_type = data.get('device_type')
        service_provider_data = data.get('service_provider_data')
        location_data = data.get('location_data')
        qr_code = data.get('qr_code')
        
        # Inserting additional information into the qr_additional_info table
        mycursor = mydb.cursor()
        mycursor.execute("INSERT INTO qr_additional_info (first_name, last_name, email, phone_number, device_id, device_type, service_provider_data, location_data, qr_code) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                         (first_name, last_name, email, phone_number, device_id, device_type, service_provider_data, location_data, qr_code))
        mydb.commit()

        return jsonify({'message': 'QR code data updated successfully'})

# Run Flask app
if __name__ == '__main__':
    print("Connected")
    app.run(debug=True)
