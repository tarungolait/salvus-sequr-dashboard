from flask import Flask, jsonify, request
from flask_cors import CORS
from Crypto.Cipher import AES
import psycopg2
import base64
import sys
import random
from Crypto.PublicKey import RSA

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

# 2.This Flask route receives user details entered after scanning QRCode
@app.route('/userdetail', methods=['POST','GET'])
def user_post():
	if request.method == 'POST': #method to be posted
		df3 = request.get_json(force=True) #displaying messgage as successful
		name = df3['Name']
		lastname = df3['Lastname']
		email = df3['Email']
		phone = df3['phone']
		device_id = df3['device_id']
		barcodeno = df3['barcodeno']
		product = df3['Product']
		#verify if the scanned qr code info is already present in the Infinicuemastertable.
		mycursor = mydb.cursor()
		mycursor.execute("ROLLBACK")
		mydb.commit()
		mycursor.execute('select barcodeno,passkey,name,email,phone,device_id,qrcode,ble_mac_id from infinicue_master_table where barcodeno=%s and product =%s',[barcodeno,product])
		existing_data = mycursor.fetchone()
		#if it is not there in the infinicuemastertable. Start generating new passkey using four quadrants data.
		if not existing_data:
			mycursor.execute('select passkey,name,email,phone,device_id,pubkey,privkey from infinicue_master_table where device_id=%s and product=%s',[device_id,product])
			validation = mycursor.fetchone()
			if validation == None:
				print('done')



			else:
				
				mycursor.execute('insert into archive_passkeymastertable(device_id, name, phone, email, passkey, pubkey,privkey,barcodeno,product) values (%s,%s,%s,%s,%s,%s,%s,%s)',[validation[4],validation[1] ,validation[3],validation[2],validation[0],validation[5],validation[6],'22',product])
				mydb.commit()
			
			mycursor.execute('delete from infinicue_master_table where device_id=%s and product=%s',[device_id,product])
			mydb.commit()
			
			mycursor.execute('insert into userdata (name,email,phone,barcodeno) values (%s,%s,%s,%s)',[name,email,phone,barcodeno])
			mydb.commit()
			#store the device_id in the devicedata table along with barcode as a primary key.
			
			mycursor.execute('insert into devicedata(device_id, barcodeno) values(%s,%s)',[device_id,barcodeno])
			mydb.commit()
			#fetch all the columns from userdata table to generate 1/4 string of a passkey.
			
			mycursor.execute("select * from userdata where barcodeno = %s", [barcodeno])
			obj2 = mycursor.fetchall()
			barcode = obj2[0]
			for row2 in obj2:
				data1 = row2[0]
				data2 = row2[1]
				data3 = row2[2]
				data4 = row2[3]
			final_2 = data1+data2+data3+data4
			ltre = ['@','.']
			for i in ltre:
				final_2 = final_2.replace(i, '')
			passkeyval_2 = random.choice(final_2)
			passkeyfor3 = random.choices(final_2,k=2)
			my_3st_str = ''.join(map(str, passkeyfor3))
			passkey_16digit_1 = random.choices(final_2,k=3)
			my_final1_passkey16 = ''.join(map(str, passkey_16digit_1))
			#fetch all the co lumns from barcode table to generate 1/4 string of a passkey.
			mycursor11 = mydb.cursor()
			mycursor11.execute("select * from barcode where barcodeno = %s", [barcodeno])
			obj = mycursor11.fetchall()
			for row in obj:
				data1 = row[0]
				data2 = row[1]
				data3 = row[2]
				data4 = row[3]
			final = data1+data2+data3+data4
			final_m = final.replace(':', '')
			passkeyval = random.choice(final_m)
			passkeyfor8 = random.choices(final_m,k=2)
			my_lst_str = ''.join(map(str, passkeyfor8) )
			passkey_16digit_3 = random.choices(final_m,k=3)
			my_final3_passkey16 = ''.join(map(str, passkey_16digit_3))
			#fetch all the columns from qrcode table to generate 1/4 string of a passkey.
			mycursor12=mydb.cursor()
			mycursor12.execute("select * from qrcode where barcodeno = %s", [barcodeno])
			obj1 = mycursor12.fetchall()
			for row1 in obj1:
				data1 = row1[0] 
				data2 = row1[1]
				data3 = row1[2]
				data4 = row1[3]
			final_1 = data1+data2+data3+data4
			final_n = final_1.replace(':', '')
			passkeyval_1 = random.choice(final_n)
			passkeyfor4 = random.choices(final_n,k=2)
			my_2st_str = ''.join(map(str, passkeyfor4))
			passkey_16digit_2 = random.choices(final_n,k=3)
			my_final2_passkey16 = ''.join(map(str, passkey_16digit_2))
			#fetch all the 
			#columns from devicedata table to generate 1/4 string of a passkey.
			mycursor14=mydb.cursor()
			mycursor14.execute("select * from devicedata where barcodeno =%s",[barcodeno])
			obj3 = mycursor14.fetchone()
			#for row3 in obj3:
			data1 = obj3[0]
			data2 = obj3[1]
			final_3 = data2+data1
			num = final_3.replace(':', '')
			passkeyval_3 = random.choice(num)
			#passkeyfor2 = random.choices(num,k=2)
			passkeyfor2 = random.sample(num,k=2)
			my_4st_str = ''.join(map(str, passkeyfor2))
			passkey_16digit = random.choices(num,k=3)
			my_final_passkey16 = ''.join(map(str, passkey_16digit))
			final_passkey = passkeyval_3+passkeyval_2+passkeyval_1+passkeyval
			digitpasskey = my_lst_str+my_2st_str+my_3st_str+my_4st_str
			digit_pass = my_final3_passkey16+my_final2_passkey16+my_final1_passkey16+my_final_passkey16  #Final passkey
			def excel_format(num):
				res = ""
				while num:
					mod = (num - 1) % 26
					res = chr(65 + mod) + res
					num = (num - mod) // 260
					return res
			def full_format(num, d=4):
				chars = num // (10**d-1) + 1 # this becomes   A..ZZZ
				digit = num %  (10**d-1) + 1 # this becomes 001..999
				return excel_format(chars) + "{:0{}d}".format(digit, d)
			x = []
			for i in range(0, 25400):
				final_8digit_passkey = (full_format(i, d=3))
				x.append(final_8digit_passkey)
			mycursor14=mydb.cursor()
			mycursor14.execute("SELECT COUNT(distinct id) FROM random")
			q = mycursor14.fetchone()
			a = q
			b =  ", ".join(map(str, a))
			c = int(b)
			#insert full passkey and partial generated passkey (without A000). 
			mycursor15 = mydb.cursor()
			q1 = mycursor15.execute("INSERT INTO random (passkey,randompasskey)VALUES(%s,%s)",((x[c]),digitpasskey))
			mydb.commit()
			final_val_passkey = x[c] + digitpasskey
			#12 digits passkey value 
			passkey = final_val_passkey
			private_key = RSA.generate(1024)
			public_key = private_key.publickey()
			private_str = private_key.export_key().decode()
			public_str = public_key.export_key().decode()
			
			mycursor.execute('insert into infinicue_master_table (barcodeno, qrcode, ble_mac_id, device_id, name, phone, email, passkey, pubkey,privkey,product) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',[barcodeno,obj1[0][0],obj1[0][1], device_id,name ,phone,email,passkey,public_str,private_str,product])
			mydb.commit() 
			return {'message' : 'successful'}

		#if user changes the device. barcode will be same but device_id is different. In that case, this condition is appilicable.
		elif device_id!=existing_data[5] and existing_data[0] == barcodeno:
			#insert the device_id into devicedata table.
			
			mycursor.execute('select passkey,name,email,phone,device_id,pubkey,privkey from infinicue_master_table where phone=%s and product=%s',[phone,product])
			validation = mycursor.fetchone()
			if validation == None:
				print('done')
			else:
				
				mycursor.execute('insert into archive_passkeymastertable(device_id, name, phone, email, passkey, pubkey,privkey,barcodeno,product) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)',[validation[4],validation[1] ,validation[3],validation[2],validation[0],validation[5],validation[6],'22',product])
				mydb.commit()
			#insert the device_id into devicedata table.
			
			mycursor.execute('delete from infinicue_master_table where phone=%s and product=%s',[phone,product])
			mydb.commit()
			
			mycursor.execute('insert into devicedata(device_id,barcodeno) values (%s,%s)',[device_id,barcodeno])
			mydb.commit()

			
			mycursor.execute('insert into archive_device(device_id,barcodeno)select device_id, barcodeno from devicedata where device_id=%s',[existing_data[5]])
			mydb.commit()

			
			mycursor.execute('delete from devicedata where device_id=%s',[existing_data[5]])
			mydb.commit()

			#fetch all the columns from userdata table to generate 1/4 string of a passkey.
			mycursor.execute("select * from userdata where barcodeno = %s", [barcodeno])
			obj2 = mycursor.fetchall()
			barcode = obj2[0]
			for row2 in obj2:
				data1 = row2[0]
				data2 = row2[1]
				data3 = row2[2]
				data4 = row2[3]
			final_2 = data1+data2+data3+data4
			ltre = ['@','.']
			for i in ltre:
				final_2 = final_2.replace(i, '')
			passkeyval_2 = random.choice(final_2)
			passkeyfor3 = random.choices(final_2,k=2)
			my_3st_str = ''.join(map(str, passkeyfor3))
			passkey_16digit_1 = random.choices(final_2,k=3)
			my_final1_passkey16 = ''.join(map(str, passkey_16digit_1))
			mycursor11 = mydb.cursor()
			#fetch all the columns from barcode table to generate 1/4 string of a passkey.
			mycursor11.execute("select * from barcode where barcodeno = %s", [barcodeno])
			obj = mycursor11.fetchall()
			for row in obj:
				data1 = row[0]
				data2 = row[1]
				data3 = row[2]
				data4 = row[3]
			final = data1+data2+data3+data4
			final_m = final.replace(':', '')
			passkeyval = random.choice(final_m)
			passkeyfor8 = random.choices(final_m,k=2)
			my_lst_str = ''.join(map(str, passkeyfor8) )
			passkey_16digit_3 = random.choices(final_m,k=3)
			my_final3_passkey16 = ''.join(map(str, passkey_16digit_3))
			#fetch all the columns from qrcodetable to generate 1/4 string of a passkey.
			mycursor12=mydb.cursor()
			mycursor12.execute("select * from qrcode where barcodeno = %s", [barcodeno])
			obj1 = mycursor12.fetchall()
			for row1 in obj1:
				data1 = row1[0] 
				data2 = row1[1]
				data3 = row1[2]
				data4 = row1[3]
			final_1 = data1+data2+data3+data4
			final_n = final_1.replace(':', '')
			passkeyval_1 = random.choice(final_n)
			passkeyfor4 = random.choices(final_n,k=2)
			my_2st_str = ''.join(map(str, passkeyfor4))
			passkey_16digit_2 = random.choices(final_n,k=3)
			my_final2_passkey16 = ''.join(map(str, passkey_16digit_2))
			#fetch all the columns from devicedata table to generate 1/4 string of a passkey.
			mycursor14=mydb.cursor()
			mycursor14.execute("select device_id,barcodeno from devicedata where barcodeno =%s",[barcodeno])
			obj3 = mycursor14.fetchone()
			for row3 in obj3:
				data1 = row3[0]
				data2 = row3[1]
			final_3 = data1+data2
			num = final_3.replace(':', '')
			passkeyval_3 = random.choice(num)
			passkeyfor2 = random.choices(num,k=2)
			my_4st_str = ''.join(map(str, passkeyfor2))
			passkey_16digit = random.choices(num,k=3)
			my_final_passkey16 = ''.join(map(str, passkey_16digit))
			existing_barcode = existing_data[0]
			existing_passkey = existing_data[1]
			existing_name = existing_data[2]
			existing_email = existing_data[3]
			existing_phone = existing_data[4]
			existing_device_id = existing_data[5]
			existing_qr_code = existing_data[6]
			existing_mac_id = existing_data[7]
			key_chan = existing_passkey[0:4]
			new_chan = key_chan+ my_lst_str+my_2st_str+my_3st_str+my_4st_str
			private_key = RSA.generate(1024)
			public_key = private_key.publickey()
			private_str = private_key.export_key().decode()
			public_str = public_key.export_key().decode()
			ab = len(private_str)
			bc = len(public_str)
			mycursor1 = mydb.cursor()
			mycursor1.execute('insert into infinicue_master_table(barcodeno,qrcode, ble_mac_id, device_id, name, phone, email, passkey,pubkey,privkey,product) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',[barcodeno,existing_qr_code,existing_mac_id,device_id,name,phone,email,new_chan,public_str,private_str,product])
			mydb.commit()
			mycursor2 = mydb.cursor()
			mycursor2.execute('insert into archive_passkeymastertable(barcodeno,qr_code,ble_mac_id,device_id,name, phone, email, passkey,pubkey,privkey,product)select barcodeno,qrcode,ble_mac_id,device_id,name,phone,email,passkey,pubkey,privkey.product from infinicue_temporary_table where device_id=%s and product=%s',[existing_data[5],product])
			mydb.commit()
			return {'message' : 'successful'}
			#return user detail to the front end.
		else:
			existing_passkey = existing_data[1]
			existing_name = existing_data[2]
			existing_email = existing_data[3]
			existing_phone = existing_data[4]
			return {'message' : 'successful'} 


# Run Flask app
if __name__ == '__main__':
    print("Connected")
    app.run(debug=True)
