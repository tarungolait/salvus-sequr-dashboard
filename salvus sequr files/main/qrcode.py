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

# Function to handle QR code data
@app.route('/')
def index():
    return 'Connected'

@app.route('/post', methods=['POST'])
def qr_code():
    if request.method == 'POST':
        # Get JSON data from request
        df2 = request.get_json(force=True)
        df1 = df2.get('QRcode')

        # Decode and decrypt QR code data
        ff = base64.b64decode(df1)
        key = 'helloworldhelloo'.encode('utf-8')
        iv = 'helloworldhelloo'.encode('utf-8')
        aes = AES.new(key, AES.MODE_CBC, iv)
        en = aes.decrypt(ff)
        en_str = en.decode('utf-8')

        # Extract data from decrypted string
        QR_code = en_str.split(',')
        qr_code = QR_code[0]
        ble_mac_id = QR_code[1]
        barcode_no = QR_code[2]
        version = QR_code[3]
        product = QR_code[4]
        device_idd = QR_code[5]

        # Database operations
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

# Run Flask app
if __name__ == '__main__':
    print("Connected")
    app.run(debug=True)
