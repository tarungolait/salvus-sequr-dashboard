import psycopg2
from barcode import EAN13
import pyqrcode
from Crypto.Cipher import AES
import base64

# Define variables
wallet_type = 'BW01'
walletcolor = 'Black'
manufacturingdate = '09-09-2021'
batchnum = '012003202102'
barcodeno = '890201700006'
countrycode = '890'
newcode99 = "NewBasicbr"
qrcode = '00002'
blemacid = '60:A4:23:32:0A:AF'
version = '1.0'
ty = 'BW01'

try:
    # Connect to PostgreSQL database
    connection = psycopg2.connect(user="postgres",
                                  password="zaynmalik2002",
                                  host="localhost",
                                  port="5432",
                                  database="infinicue")
    cursor = connection.cursor()

    # Generate barcode
    my_code = EAN13(barcodeno)
    my_code.save(newcode99)

    # Insert data into barcode table
    postgres_insert_query = """INSERT INTO barcode (wallet_type, walletcolor, manufacturingdate, batchnum, countrycode, barcodeno) VALUES (%s,%s,%s,%s,%s,%s)"""
    record_to_insert = (wallet_type, walletcolor, manufacturingdate, batchnum, countrycode, barcodeno)
    cursor.execute(postgres_insert_query, record_to_insert)

    # Generate QR code
    site = [qrcode, ',', blemacid, ',', barcodeno, ',', version, ',', ty, ',', ',\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10']
    str_qr = ''.join(site)
    qr_byte = str_qr.encode('utf-8')
    key = 'helloworldhelloo'.encode('utf-8')
    iv = 'helloworldhelloo'.encode('utf-8')
    aes = AES.new(key, AES.MODE_CBC, iv)
    en = aes.encrypt(qr_byte)
    fg = str(base64.encodebytes(en), encoding='utf-8')
    getqrcode = pyqrcode.create(fg)
    getqrcode.svg("NewBasicQR.svg", scale=10)

    # Insert data into qrcode table
    postgres_insert_query = """INSERT INTO qrcode (qrcode, ble_mac_id, barcodeno, version, type) VALUES (%s,%s,%s,%s,%s)"""
    record_to_insert = (qrcode, blemacid, barcodeno, version, ty)
    cursor.execute(postgres_insert_query, record_to_insert)

    # Insert data into infinicue_master_table
    postgres_insert_query = """INSERT INTO infinicue_master_table (barcodeno, ble_mac_id, qrcode, product) VALUES (%s, %s, %s, %s)"""
    record_to_insert = (barcodeno, blemacid, qrcode, ty)
    cursor.execute(postgres_insert_query, record_to_insert)

    # Commit changes and close connection
    connection.commit()
    count = cursor.rowcount
    print(count, "Record inserted successfully into barcode and qrcode tables")

except psycopg2.Error as error:
    print("Failed to insert record:", error)

finally:
    # Close database connection
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
