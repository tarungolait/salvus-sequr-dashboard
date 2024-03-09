from flask import Flask, jsonify, request
from flask_cors import CORS
from Crypto.PublicKey import RSA
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

app.config['SECRET_KEY'] = 'Infinicue'
app.config['SESSION_COOKIE_SECURE'] = True

@app.route('/userdetail', methods=['POST','GET'])
def user_details():
    if request.method == 'POST':
        user_data = request.get_json(force=True)
        name = user_data['Name']
        lastname = user_data['Lastname']
        email = user_data['Email']
        phone = user_data['phone']
        device_id = user_data['device_id']
        barcodeno = user_data['barcodeno']
        product = user_data['Product']

        cursor = connection.cursor()
        cursor.execute("ROLLBACK")
        connection.commit()

        cursor.execute('SELECT barcodeno, passkey, name, email, phone, device_id, qrcode, ble_mac_id FROM infinicue_master_table WHERE barcodeno=%s AND product=%s', [barcodeno, product])
        existing_data = cursor.fetchone()

        if not existing_data:
            cursor.execute('SELECT passkey, name, email, phone, device_id, pubkey, privkey FROM infinicue_master_table WHERE device_id=%s AND product=%s', [device_id, product])
            validation = cursor.fetchone()
            if validation == None:
                print('Validation failed')
            else:
                cursor.execute('INSERT INTO archive_passkeymastertable (device_id, name, phone, email, passkey, pubkey, privkey, barcodeno, product) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)', [validation[4], validation[1], validation[3], validation[2], validation[0], validation[5], validation[6], '22', product])
                connection.commit()

            cursor.execute('DELETE FROM infinicue_master_table WHERE device_id=%s AND product=%s', [device_id, product])
            connection.commit()

            cursor.execute('INSERT INTO userdata (name, email, phone, barcodeno) VALUES (%s, %s, %s, %s)', [name, email, phone, barcodeno])
            connection.commit()

            cursor.execute('INSERT INTO devicedata (device_id, barcodeno) VALUES (%s, %s)', [device_id, barcodeno])
            connection.commit()

            cursor.execute("SELECT * FROM userdata WHERE barcodeno = %s", [barcodeno])
            user_data_row = cursor.fetchall()
            barcode = user_data_row[0]
            for row in user_data_row:
                data1 = row[0]
                data2 = row[1]
                data3 = row[2]
                data4 = row[3]
            final_data = data1 + data2 + data3 + data4
            special_characters = ['@', '.']
            for char in special_characters:
                final_data = final_data.replace(char, '')
            passkey_val_2 = random.choice(final_data)
            passkey_for_3 = random.choices(final_data, k=2)
            my_3rd_string = ''.join(map(str, passkey_for_3))
            passkey_16_digit_1 = random.choices(final_data, k=3)
            my_final_1_passkey_16 = ''.join(map(str, passkey_16_digit_1))

            cursor.execute("SELECT * FROM barcode WHERE barcodeno = %s", [barcodeno])
            barcode_data_row = cursor.fetchall()
            for row in barcode_data_row:
                data1 = row[0]
                data2 = row[1]
                data3 = row[2]
                data4 = row[3]
            final_barcode_data = data1 + data2 + data3 + data4
            final_modified_data = final_barcode_data.replace(':', '')
            passkey_val = random.choice(final_modified_data)
            passkey_for_8 = random.choices(final_modified_data, k=2)
            my_lst_str = ''.join(map(str, passkey_for_8))
            passkey_16_digit_3 = random.choices(final_modified_data, k=3)
            my_final_3_passkey_16 = ''.join(map(str, passkey_16_digit_3))

            cursor.execute("SELECT * FROM qrcode WHERE barcodeno = %s", [barcodeno])
            qrcode_data_row = cursor.fetchall()
            for row in qrcode_data_row:
                data1 = row[0]
                data2 = row[1]
                data3 = row[2]
                data4 = row[3]
            final_qrcode_data = data1 + data2 + data3 + data4
            final_qrcode_modified_data = final_qrcode_data.replace(':', '')
            passkey_val_1 = random.choice(final_qrcode_modified_data)
            passkey_for_4 = random.choices(final_qrcode_modified_data, k=2)
            my_2nd_str = ''.join(map(str, passkey_for_4))
            passkey_16_digit_2 = random.choices(final_qrcode_modified_data, k=3)
            my_final_2_passkey_16 = ''.join(map(str, passkey_16_digit_2))

            cursor.execute("SELECT device_id, barcodeno FROM devicedata WHERE barcodeno = %s", [barcodeno])
            devicedata_row = cursor.fetchone()
            data1 = devicedata_row[0]
            data2 = devicedata_row[1]
            final_3 = data1 + data2
            modified_final_3 = final_3.replace(':', '')
            passkey_val_3 = random.choice(modified_final_3)
            passkey_for_2 = random.choices(modified_final_3, k=2)
            my_4th_str = ''.join(map(str, passkey_for_2))
            passkey_16_digit = random.choices(modified_final_3, k=3)
            my_final_passkey_16 = ''.join(map(str, passkey_16_digit))
            final_passkey = passkey_val_3 + passkey_val_2 + passkey_val_1 + passkey_val
            digit_passkey = my_lst_str + my_2nd_str + my_3rd_string + my_4th_str
            digit_pass = my_final_3_passkey_16 + my_final_2_passkey_16 + my_final_1_passkey_16 + my_final_passkey_16

            def excel_format(num):
                res = ""
                while num:
                    mod = (num - 1) % 26
                    res = chr(65 + mod) + res
                    num = (num - mod) // 260
                    return res

            def full_format(num, d=4):
                chars = num // (10**d-1) + 1
                digit = num %  (10**d-1) + 1
                return excel_format(chars) + "{:0{}d}".format(digit, d)

            x = []
            for i in range(0, 25400):
                final_8digit_passkey = (full_format(i, d=3))
                x.append(final_8digit_passkey)

            cursor.execute("SELECT COUNT(distinct id) FROM random")
            q = cursor.fetchone()
            a = q
            b =  ", ".join(map(str, a))
            c = int(b)

            cursor.execute("INSERT INTO random (passkey, randompasskey) VALUES (%s, %s)", ((x[c]), digit_passkey))
            connection.commit()
            final_val_passkey = x[c] + digit_passkey
            passkey = final_val_passkey
            private_key = RSA.generate(1024)
            public_key = private_key.publickey()
            private_str = private_key.export_key().decode()
            public_str = public_key.export_key().decode()
            
            
            if qrcode_data_row:
                # Check if qrcode_data_row has elements before accessing its indices
                qrcode_value = qrcode_data_row[0][0] if len(qrcode_data_row[0]) > 0 else None
                ble_mac_id = qrcode_data_row[0][1] if len(qrcode_data_row[0]) > 1 else None
            else:
                # Handle the case where qrcode_data_row is empty
                qrcode_value = None
                ble_mac_id = None
                
            cursor.execute("INSERT INTO infinicue_master_table (barcodeno, qrcode, ble_mac_id, device_id, name, phone, email, passkey, pubkey, privkey, product) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", [barcodeno, qrcode_value, ble_mac_id, device_id, name, phone, email, passkey, public_str, private_str, product])
            connection.commit() 
            return jsonify({'message': 'Successful'})

        elif device_id != existing_data[5] and existing_data[0] == barcodeno:
            cursor.execute('SELECT passkey, name, email, phone, device_id, pubkey, privkey FROM infinicue_master_table WHERE phone=%s AND product=%s', [phone, product])
            validation = cursor.fetchone()
            if validation == None:
                print('Validation failed')
            else:
                cursor.execute('INSERT INTO archive_passkeymastertable (device_id, name, phone, email, passkey, pubkey, privkey, barcodeno, product) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)', [validation[4], validation[1], validation[3], validation[2], validation[0], validation[5], validation[6], '22', product])
                connection.commit()

            cursor.execute('DELETE FROM infinicue_master_table WHERE phone=%s AND product=%s', [phone, product])
            connection.commit()

            cursor.execute('INSERT INTO devicedata (device_id, barcodeno) VALUES (%s, %s)', [device_id, barcodeno])
            connection.commit()

            cursor.execute('INSERT INTO archive_device (device_id, barcodeno) SELECT device_id, barcodeno FROM devicedata WHERE device_id=%s', [existing_data[5]])
            connection.commit()

            cursor.execute('DELETE FROM devicedata WHERE device_id=%s', [existing_data[5]])
            connection.commit()

            cursor.execute("SELECT * FROM userdata WHERE barcodeno = %s", [barcodeno])
            user_data_row = cursor.fetchall()
            barcode = user_data_row[0]
            for row in user_data_row:
                data1 = row[0]
                data2 = row[1]
                data3 = row[2]
                data4 = row[3]
            final_data = data1 + data2 + data3 + data4
            special_characters = ['@', '.']
            for char in special_characters:
                final_data = final_data.replace(char, '')
            passkey_val_2 = random.choice(final_data)
            passkey_for_3 = random.choices(final_data, k=2)
            my_3rd_string = ''.join(map(str, passkey_for_3))
            passkey_16_digit_1 = random.choices(final_data, k=3)
            my_final_1_passkey_16 = ''.join(map(str, passkey_16_digit_1))

            cursor.execute("SELECT * FROM barcode WHERE barcodeno = %s", [barcodeno])
            barcode_data_row = cursor.fetchall()
            for row in barcode_data_row:
                data1 = row[0]
                data2 = row[1]
                data3 = row[2]
                data4 = row[3]
            final_barcode_data = data1 + data2 + data3 + data4
            final_modified_data = final_barcode_data.replace(':', '')
            passkey_val = random.choice(final_modified_data)
            passkey_for_8 = random.choices(final_modified_data, k=2)
            my_lst_str = ''.join(map(str, passkey_for_8))
            passkey_16_digit_3 = random.choices(final_modified_data, k=3)
            my_final_3_passkey_16 = ''.join(map(str, passkey_16_digit_3))

            cursor.execute("SELECT * FROM qrcode WHERE barcodeno = %s", [barcodeno])
            qrcode_data_row = cursor.fetchall()
            for row in qrcode_data_row:
                data1 = row[0]
                data2 = row[1]
                data3 = row[2]
                data4 = row[3]
            final_qrcode_data = data1 + data2 + data3 + data4
            final_qrcode_modified_data = final_qrcode_data.replace(':', '')
            passkey_val_1 = random.choice(final_qrcode_modified_data)
            passkey_for_4 = random.choices(final_qrcode_modified_data, k=2)
            my_2nd_str = ''.join(map(str, passkey_for_4))
            passkey_16_digit_2 = random.choices(final_qrcode_modified_data, k=3)
            my_final_2_passkey_16 = ''.join(map(str, passkey_16_digit_2))

            cursor.execute("SELECT device_id, barcodeno FROM devicedata WHERE barcodeno = %s", [barcodeno])
            devicedata_row = cursor.fetchone()
            data1 = devicedata_row[0]
            data2 = devicedata_row[1]
            final_3 = data1 + data2
            modified_final_3 = final_3.replace(':', '')
            passkey_val_3 = random.choice(modified_final_3)
            passkey_for_2 = random.choices(modified_final_3, k=2)
            my_4th_str = ''.join(map(str, passkey_for_2))
            passkey_16_digit = random.choices(modified_final_3, k=3)
            my_final_passkey_16 = ''.join(map(str, passkey_16_digit))
            existing_barcode = existing_data[0]
            existing_passkey = existing_data[1]
            existing_name = existing_data[2]
            existing_email = existing_data[3]
            existing_phone = existing_data[4]
            existing_device_id = existing_data[5]
            existing_qr_code = existing_data[6]
            existing_mac_id = existing_data[7]
            key_chan = existing_passkey[0:4]
            new_chan = key_chan + my_lst_str + my_2nd_str + my_3rd_string + my_4th_str
            private_key = RSA.generate(1024)
            public_key = private_key.publickey()
            private_str = private_key.export_key().decode()
            public_str = public_key.export_key().decode()

            cursor.execute('INSERT INTO infinicue_master_table (barcodeno, qrcode, ble_mac_id, device_id, name, phone, email, passkey, pubkey, privkey, product) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', [barcodeno, existing_qr_code, existing_mac_id, device_id, name, phone, email, new_chan, public_str, private_str, product])
            connection.commit()

            cursor.execute('INSERT INTO archive_passkeymastertable (barcodeno, qr_code, ble_mac_id, device_id, name, phone, email, passkey, pubkey, privkey, product) SELECT barcodeno, qrcode, ble_mac_id, device_id, name, phone, email, passkey, pubkey, privkey, product FROM infinicue_temporary_table WHERE device_id=%s AND product=%s', [existing_data[5], product])
            connection.commit()

            return jsonify({'message': 'Successful'})

        else:
            existing_passkey = existing_data[1]
            existing_name = existing_data[2]
            existing_email = existing_data[3]
            existing_phone = existing_data[4]
            return jsonify({'message': 'Successful'}) 

if __name__ == '__main__':
    app.run(debug=True)
