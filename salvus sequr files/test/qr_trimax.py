import pyqrcode #To generate QRcode through python script

import json     #To give key value pairs json is imported

import psycopg2 #To connect database in postgres

from Crypto.Cipher import AES #To import encrypting algorithms

import base64   #To convert binary to ASCII

import sys      #To provide name of existing modules that have been alreday installed

#'60:A4:23:32:0B:62'

qrcode = '00002' #declaring variables globally

blemacid = '60:A4:23:32:0A:AF'

barcodeno = '890201700003'

version = '1.0'

ty = 'BW01'



try:

   connection = psycopg2.connect(user="postgres", #inserting database credentials like localhost,username,password and port num as given in postgres

                                  password="zaynmalik2002",

                                  host="localhost",

                                  port="5432",

                                  database="infinicue")

   cursor = connection.cursor()  #establishing connection



except psycopg2.Error as e:      #exception error 

	print('Unable to connect with database due to',e)

	sys.exit()

site = [qrcode,',',blemacid,',',barcodeno,',',version,',',ty,',',',\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10']

str_qr = ''.join(site)

qr_byte = str_qr.encode('utf-8')

key = 'helloworldhelloo'.encode('utf-8') #encrypted algorithm uses key

iv = 'helloworldhelloo'.encode('utf-8')  #Value used for decryption

aes = AES.new(key,AES.MODE_CBC,iv)

en = aes.encrypt(qr_byte)

fg = str(base64.encodebytes(en),encoding='utf-8')

getqrcode = pyqrcode.create(fg)

getqrcode.svg("NewBasicQR.svg", scale =10)

postgres_insert_query = """ INSERT INTO qrcode (qrcode, ble_mac_id, barcodeno,version,type) VALUES (%s,%s,%s,%s,%s)"""

record_to_insert = (qrcode,blemacid,barcodeno,version,ty) #inserting of data into postgres tables

cursor.execute(postgres_insert_query, record_to_insert)

connection.commit()

count = cursor.rowcount

print (count, "Record inserted successfully into qrcode table")







