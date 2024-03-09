from flask import Flask, jsonify, request
from Crypto.Cipher import AES
import base64
import psycopg2

app = Flask(__name__)

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

# Run Flask app
if __name__ == '__main__':
    app.run(debug=True)
