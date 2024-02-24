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
    mydb = psycopg2.connect(
        host="localhost",
        port=5432,
        database="infinicue",
        user="postgres",
        password="zaynmalik2002"
    )
except psycopg2.Error as e:
    print('Unable to connect with database due to', e)
    sys.exit()

app.config['SECRET_KEY'] = 'Infinicue'
app.config['SESSION_COOKIE_SECURE'] = True

def generate_passkey(length):
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    return ''.join(random.choice(characters) for _ in range(length))

def generate_passkey16():
    return ''.join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", k=16))

def generate_passkey_4parts(data):
    return ''.join(random.choices(data.replace('@', '').replace('.', ''), k=2))

def generate_full_format(num, d=4):
    chars = num // (10 ** d - 1) + 1
    digit = num % (10 ** d - 1) + 1
    return chr(65 + chars - 1) + "{:0{}d}".format(digit, d)

def generate_full_passkey():
    return generate_full_format(random.randint(0, 25400), 3)

@app.route('/userdetail', methods=['POST'])
def user_post():
    if request.method == 'POST':
        data = request.get_json(force=True)

        name = data['Name']
        lastname = data['Lastname']
        email = data['Email']
        phone = data['phone']
        device_id = data['device_id']
        barcodeno = data['barcodeno']
        product = data['Product']

        mycursor = mydb.cursor()

        mycursor.execute("ROLLBACK")
        mydb.commit()

        mycursor.execute('select barcodeno,passkey,name,email,phone,device_id,qrcode,ble_mac_id from infinicue_master_table where barcodeno=%s and product =%s', [barcodeno, product])
        existing_data = mycursor.fetchone()

        if not existing_data:
            mycursor.execute('select passkey,name,email,phone,device_id,pubkey,privkey from infinicue_master_table where device_id=%s and product=%s', [device_id, product])
            validation = mycursor.fetchone()

            if validation is None:
                print('done')
            else:
                mycursor.execute('insert into archive_passkeymastertable(device_id, name, phone, email, passkey, pubkey,privkey,barcodeno,product) values (%s,%s,%s,%s,%s,%s,%s,%s)', [validation[4], validation[1], validation[3], validation[2], validation[0], validation[5], validation[6], '22', product])
                mydb.commit()

            mycursor.execute('delete from infinicue_master_table where device_id=%s and product=%s', [device_id, product])
            mydb.commit()

            mycursor.execute('insert into userdata (name,email,phone,barcodeno) values (%s,%s,%s,%s)', [name, email, phone, barcodeno])
            mydb.commit()

            mycursor.execute('insert into devicedata(device_id, barcodeno) values(%s,%s)', [device_id, barcodeno])
            mydb.commit()

            obj2 = mycursor.execute("select * from userdata where barcodeno = %s", [barcodeno])
            final_2 = ''.join(''.join(row[:3]) for row in obj2).replace('@', '').replace('.', '')
            passkeyval_2 = random.choice(final_2)
            passkeyfor3 = generate_passkey_4parts(final_2)
            my_3st_str = ''.join(passkeyfor3)
            passkey_16digit_1 = generate_passkey16()
            my_final1_passkey16 = ''.join(passkey_16digit_1)

            mycursor11 = mydb.cursor()
            obj = mycursor11.execute("select * from barcode where barcodeno = %s", [barcodeno])
            final = ''.join(''.join(row[:3]) for row in obj).replace(':', '')
            passkeyval = random.choice(final)
            passkeyfor8 = generate_passkey_4parts(final)
            my_lst_str = ''.join(passkeyfor8)
            passkey_16digit_3 = generate_passkey16()
            my_final3_passkey16 = ''.join(passkey_16digit_3)

            mycursor12 = mydb.cursor()
            obj1 = mycursor12.execute("select * from qrcode where barcodeno = %s", [barcodeno])
            final_1 = ''.join(''.join(row[:3]) for row in obj1).replace(':', '')
            passkeyval_1 = random.choice(final_1)
            passkeyfor4 = generate_passkey_4parts(final_1)
            my_2st_str = ''.join(passkeyfor4)
            passkey_16digit_2 = generate_passkey16()
            my_final2_passkey16 = ''.join(passkey_16digit_2)

            mycursor14 = mydb.cursor()
            mycursor14.execute("select * from devicedata where barcodeno =%s", [barcodeno])
            obj3 = mycursor14.fetchone()
            final_3 = ''.join(obj3)
            passkeyval_3 = random.choice(final_3)
            passkeyfor2 = generate_passkey_4parts(final_3)
            my_4st_str = ''.join(passkeyfor2)
            passkey_16digit = generate_passkey16()
            my_final_passkey16 = ''.join(passkey_16digit)

            final_passkey = passkeyval_3 + passkeyval_2 + passkeyval_1 + passkeyval
            digitpasskey = my_lst_str + my_2st_str + my_3st_str + my_4st_str
            digit_pass = my_final3_passkey16 + my_final2_passkey16 + my_final1_passkey16 + my_final_passkey16

            mycursor14 = mydb.cursor()
            mycursor14.execute("SELECT COUNT(distinct id) FROM random")
            q = mycursor14.fetchone()
            c = int(q[0])
            x = [generate_full_format(i, d=3) for i in range(25400)]
            mycursor15 = mydb.cursor()
            q1 = mycursor15.execute("INSERT INTO random (passkey,randompasskey)VALUES(%s,%s)", ((x[c]), digitpasskey))
            mydb.commit()
            final_val_passkey = x[c] + digitpasskey
            passkey = final_val_passkey
            private_key = RSA.generate(1024)
            public_key = private_key.publickey()
            private_str = private_key.export_key().decode()
            public_str = public_key.export_key().decode()

            mycursor.execute('insert into infinicue_master_table (barcodeno, qrcode, ble_mac_id, device_id, name, phone, email, passkey, pubkey,privkey,product) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', [barcodeno, obj1[0][0], obj1[0][1], device_id, name, phone, email, passkey, public_str, private_str, product])
            mydb.commit()
            return {'message': 'successful'}
        elif device_id != existing_data[5] and existing_data[0] == barcodeno:
            mycursor.execute('select passkey,name,email,phone,device_id,pubkey,privkey from infinicue_master_table where phone=%s and product=%s', [phone, product])
            validation = mycursor.fetchone()

            if validation is None:
                print('done')
            else:
                mycursor.execute('insert into archive_passkeymastertable(device_id, name, phone, email, passkey, pubkey,privkey,barcodeno,product) values (%s,%s,%s,%s,%s,%s,%s,%s)', [validation[4], validation[1], validation[3], validation[2], validation[0], validation[5], validation[6], '22', product])
                mydb.commit()

            mycursor.execute('delete from infinicue_master_table where phone=%s and product=%s', [phone, product])
            mydb.commit()

            mycursor.execute('insert into devicedata(device_id,barcodeno) values (%s,%s)', [device_id, barcodeno])
            mydb.commit()

            mycursor.execute('insert into archive_device(device_id,barcodeno)select device_id, barcodeno from devicedata where device_id=%s', [existing_data[5]])
            mydb.commit()

            mycursor.execute('delete from devicedata where device_id=%s', [existing_data[5]])
            mydb.commit()

            obj2 = mycursor.execute("select * from userdata where barcodeno = %s", [barcodeno])
            final_2 = ''.join(''.join(row[:3]) for row in obj2).replace('@', '').replace('.', '')
            passkeyval_2 = random.choice(final_2)
            passkeyfor3 = generate_passkey_4parts(final_2)
            my_3st_str = ''.join(passkeyfor3)
            passkey_16digit_1 = generate_passkey16()
            my_final1_passkey16 = ''.join(passkey_16digit_1)

            mycursor11 = mydb.cursor()
            obj = mycursor11.execute("select * from barcode where barcodeno = %s", [barcodeno])
            final = ''.join(''.join(row[:3]) for row in obj).replace(':', '')
            passkeyval = random.choice(final)
            passkeyfor8 = generate_passkey_4parts(final)
            my_lst_str = ''.join(passkeyfor8)
            passkey_16digit_3 = generate_passkey16()
            my_final3_passkey16 = ''.join(passkey_16digit_3)

            mycursor12 = mydb.cursor()
            obj1 = mycursor12.execute("select * from qrcode where barcodeno = %s", [barcodeno])
            final_1 = ''.join(''.join(row[:3]) for row in obj1).replace(':', '')
            passkeyval_1 = random.choice(final_1)
            passkeyfor4 = generate_passkey_4parts(final_1)
            my_2st_str = ''.join(passkeyfor4)
            passkey_16digit_2 = generate_passkey16()
            my_final2_passkey16 = ''.join(passkey_16digit_2)

            mycursor14 = mydb.cursor()
            mycursor14.execute("select device_id,barcodeno from devicedata where barcodeno =%s", [barcodeno])
            obj3 = mycursor14.fetchone()
            final_3 = ''.join(obj3)
            passkeyval_3 = random.choice(final_3)
            passkeyfor2 = generate_passkey_4parts(final_3)
            my_4st_str = ''.join(passkeyfor2)
            passkey_16digit = generate_passkey16()
            my_final_passkey16 = ''.join(passkey_16digit)

            existing_barcode = existing_data[0]
            existing_passkey = existing_data[1]
            existing_name = existing_data[2]
            existing_email = existing_data[3]
            existing_phone = existing_data[4]
            existing_device_id = existing_data[5]
            existing_qr_code = existing_data[6]
            existing_mac_id = existing_data[7]

            key_chan = existing_passkey[0:4]
            new_chan = key_chan + my_lst_str + my_2st_str + my_3st_str + my_4st_str

            private_key = RSA.generate(1024)
            public_key = private_key.publickey()
            private_str = private_key.export_key().decode()
            public_str = public_key.export_key().decode()

            mycursor1 = mydb.cursor()
            mycursor1.execute('insert into infinicue_master_table(barcodeno,qrcode, ble_mac_id, device_id, name, phone, email, passkey,pubkey,privkey,product) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', [barcodeno, existing_qr_code, existing_mac_id, device_id, name, phone, email, new_chan, public_str, private_str, product])
            mydb.commit()

            mycursor2 = mydb.cursor()
            mycursor2.execute('insert into archive_passkeymastertable(barcodeno,qr_code,ble_mac_id,device_id,name, phone, email, passkey,pubkey,privkey,product)select barcodeno,qrcode,ble_mac_id,device_id,name,phone,email,passkey,pubkey,privkey.product from infinicue_temporary_table where device_id=%s and product=%s', [existing_data[5], product])
            mydb.commit()

            return {'message': 'successful'}
        else:
            existing_passkey = existing_data[1]
            existing_name = existing_data[2]
            existing_email = existing_data[3]
            existing_phone = existing_data[4]
            return {'message': 'successful'}

if __name__ == '__main__':
    app.run(debug=True)
