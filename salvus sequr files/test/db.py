from flask import Flask,request,jsonify
import requests
import psycopg2
import json
import random
import sys
from Crypto.Cipher import AES,PKCS1_OAEP
from Crypto.PublicKey import RSA
from binascii import hexlify
import time
from datetime import date,datetime 
# from win10toast import ToastNotifier
import base64

try:
  conn = psycopg2.connect(
    host = "localhost",
    port = 5432,
    database = "infinicue",
    user = "postgres",
    password = "zaynmalik2002")
except psycopg2.Error as e:
  print('Unable to connect with database due to ', e)
  sys.exit()



cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS api_bank")
sql ='''CREATE TABLE api_bank(
   bank VARCHAR
(30) NOT NULL,
   card_type VARCHAR
(30),
   account_type VARCHAR
(30),
   phone VARCHAR
(30),
   name VARCHAR
(30),
   uuid VARCHAR
(20)
   )'''
cursor.execute(sql)
conn.commit()
print(" api_bank Table created successfully........")
# #Closing the connection
cursor.execute("DROP TABLE IF EXISTS archive_device")
sql ='''CREATE TABLE archive_device(
barcodeno VARCHAR
(30) NOT NULL,
device_id VARCHAR
(100)
)'''
cursor.execute(sql)
conn.commit()
print("archive_device Table created successfully........")
cursor.execute("DROP TABLE IF EXISTS archive_passkeymastertable")
sql ='''CREATE TABLE archive_passkeymastertable(
barcodeno VARCHAR
(30) NOT NULL,
phone VARCHAR
(30),
passkey VARCHAR
(20),
ble_mac_id VARCHAR
(20),
qr_code VARCHAR
(20),
device_id VARCHAR
(100),
email VARCHAR
(30),
name VARCHAR
(30),
pubkey VARCHAR
(2500),
privkey VARCHAR
(2500),
product VARCHAR(20)
)'''
cursor.execute(sql)
conn.commit()
print("archive_passkeymasterTable created successfully........")
cursor.execute("DROP TABLE IF EXISTS archivetable")
sql ='''CREATE TABLE archivetable(
timer VARCHAR
(30),
phone VARCHAR
(30),
ble_mac_id VARCHAR
(30),
card_type VARCHAR
(30),
date VARCHAR
(30),
bank_name VARCHAR
(30),
latitude VARCHAR
(30),
longitude VARCHAR
(30),
device_id VARCHAR
(60),
card_name VARCHAR
(20),
share VARCHAR
(30),
s_no VARCHAR
(30),
type_of_transaction VARCHAR
(30),
device_token VARCHAR
(200)
)'''
cursor.execute(sql)
conn.commit()
print("archivetable created successfully........")
cursor.execute("DROP TABLE IF EXISTS archive_tableshare")
sql ='''CREATE TABLE archive_tableshare(
bank VARCHAR
(30),
card_type VARCHAR
(30),
phone VARCHAR
(30),
s_no VARCHAR
(30),
share_phone VARCHAR
(30),
card_name VARCHAR
(30)
)'''
cursor.execute(sql)
conn.commit()
print("archive_tableshare created successfully........")
cursor.execute("DROP TABLE IF EXISTS bank")
sql ='''CREATE TABLE bank(
phone VARCHAR
(30),
password VARCHAR
(30)
)'''
cursor.execute(sql)
conn.commit()
print("bank created successfully........")
cursor.execute("DROP TABLE IF EXISTS bank_master_table")
sql ='''CREATE TABLE bank_master_table(
bank VARCHAR
(30),
card_type VARCHAR
(30),
account_type VARCHAR
(30),
phone VARCHAR
(30),
name VARCHAR
(30),
device_id VARCHAR
(60),
barcodeno VARCHAR
(30),
ble_mac_id VARCHAR
(30),
s_no VARCHAR
(30),
card_name VARCHAR
(30),
uuid VARCHAR
(30),
device_token VARCHAR
(200),
pubkey VARCHAR
(2500),
privkey VARCHAR
(2500),
key VARCHAR
(500),
product VARCHAR(20)
)'''
cursor.execute(sql)
conn.commit()
print("bank_mastertable created successfully........")
cursor.execute("DROP TABLE IF EXISTS bank_path")
sql ='''CREATE TABLE bank_path(
bank_name VARCHAR
(30),
url_verification VARCHAR
(60),
url_event VARCHAR
(60)
)'''
cursor.execute(sql)
conn.commit()
print("bank_path created successfully........")
print("bank created successfully........")
cursor.execute("DROP TABLE IF EXISTS bank_table")
sql ='''CREATE TABLE bank_table(
name VARCHAR
(30),
lastname VARCHAR
(35),
email VARCHAR
(30),
phone VARCHAR
(30),
qrcode VARCHAR
(30)
)'''
cursor.execute(sql)
conn.commit()
print("bank_table created successfully........")
cursor.execute("DROP TABLE IF EXISTS bank_temporary_table")
sql ='''CREATE TABLE bank_temporary_table(
bank VARCHAR
(30),
card_type VARCHAR
(30),
card_name VARCHAR
(30),
account_type VARCHAR
(30),
phone VARCHAR
(30),
ble_mac_id VARCHAR
(30),
device_id VARCHAR
(100),
s_no VARCHAR
(30),
barcodeno VARCHAR
(30),
uuid VARCHAR
(30),
name VARCHAR
(30),
device_token VARCHAR
(200),
pubkey VARCHAR
(2500),
privkey VARCHAR
(2500),
key VARCHAR
(500)
)'''
cursor.execute(sql)
conn.commit()
print("bank_temporary_table created successfully........")
cursor.execute("DROP TABLE IF EXISTS barcode")
sql ='''CREATE TABLE barcode(
wallet_type VARCHAR
(30),
walletcolor VARCHAR
(30),
manufacturingdate VARCHAR
(30),
batchnum VARCHAR
(30),
barcodeno VARCHAR
(30),
countrycode VARCHAR
(30)
)'''
cursor.execute(sql)
conn.commit()
print("barcode table created successfully........")
cursor.execute("DROP TABLE IF EXISTS cardback")
sql ='''CREATE TABLE cardback(
bank_name VARCHAR
(30),
card_type VARCHAR
(30),
time VARCHAR
(30),
date VARCHAR
(30),
name VARCHAR
(30),
latitude VARCHAR
(30),
longitude VARCHAR
(30),
ble_mac_id VARCHAR
(30)
)'''
cursor.execute(sql)
conn.commit()
print("cardback table created successfully........")
cursor.execute("DROP TABLE IF EXISTS cardremoval")
sql ='''CREATE TABLE cardremoval(
bank_name VARCHAR
(30),
card_type VARCHAR
(30),
time VARCHAR
(30),
date VARCHAR
(30),
latitude VARCHAR
(30),
longitude VARCHAR
(30),
ble_mac_id VARCHAR
(30),
phone VARCHAR
(30),
s_no VARCHAR
(30),
event_type VARCHAR
(30),
device_id VARCHAR
(60),
card_name VARCHAR
(30)
)'''
cursor.execute(sql)
conn.commit()
print("cardremoval table created successfully........")
cursor.execute("DROP TABLE IF EXISTS archivecardremoval")
sql ='''CREATE TABLE archivecardremoval(
bank_name VARCHAR
(30),
card_type VARCHAR
(30),
time VARCHAR
(30),
date VARCHAR
(30),
latitude VARCHAR
(30),
longitude VARCHAR
(30),
ble_mac_id VARCHAR
(30),
phone VARCHAR
(30),
s_no VARCHAR
(30),
event_type VARCHAR
(30),
device_id VARCHAR
(60),
card_name VARCHAR
(30)
)'''
cursor.execute(sql)
conn.commit()
print("archivecardremoval table created successfully........")
cursor.execute("DROP TABLE IF EXISTS cheque_data")
sql ='''CREATE TABLE cheque_data(
id SERIAL,
cheque_no VARCHAR
(30),
date_of_cheque VARCHAR
(30),
amount VARCHAR
(30),
pay_to VARCHAR
(30),
phone VARCHAR
(30),
ble_mac_id VARCHAR
(30),
device_id VARCHAR
(100),
cheque_expiry VARCHAR
(30),
image_path VARCHAR
(200),
date_of_image VARCHAR
(30),
directory VARCHAR
(100),
time1 VARCHAR(20),
date1 VARCHAR(30),
latitude VARCHAR(30),
longitude VARCHAR(30),
address VARCHAR(700),
path1 VARCHAR(1000)
)'''
cursor.execute(sql)
conn.commit()
print("cheque_data created successfully........")
cursor.execute("DROP TABLE IF EXISTS cheque_event")
sql ='''CREATE TABLE cheque_event(
ble_mac_id VARCHAR
(30),
device_id VARCHAR
(100),
phone VARCHAR
(30),
i_d VARCHAR
(30),
latitude VARCHAR
(30),
longitude VARCHAR
(30),
event_type VARCHAR
(30),
timer VARCHAR
(30)
)'''
cursor.execute(sql)
conn.commit()
print("cheque_event table created successfully.........")
cursor.execute("DROP TABLE IF EXISTS devicedata1")
sql ='''CREATE TABLE devicedata1(
device_id VARCHAR
(100),
phone VARCHAR
(30)
)'''
cursor.execute(sql)
conn.commit()
print("devicedata1 table created successfully........")
cursor.execute("DROP TABLE IF EXISTS devicedata")
sql ='''CREATE TABLE devicedata(
device_id VARCHAR
(100),
barcodeno VARCHAR
(30),
qrcode VARCHAR
(30)
)'''
cursor.execute(sql)
conn.commit()
print("devicedata table created successfully........")
cursor.execute("DROP TABLE IF EXISTS fraud")
sql ='''CREATE TABLE fraud(
bank VARCHAR
(30),
card_type VARCHAR
(20),
timer VARCHAR
(30),
date VARCHAR
(30),
latitude VARCHAR
(30),
longitude VARCHAR
(30),
device_token VARCHAR
(200),
phone VARCHAR
(30),
type_of_transaction VARCHAR
(30),
i_d VARCHAR
(30)
)'''
cursor.execute(sql)
conn.commit()
print("fraud table created successfully")
cursor.execute("DROP TABLE IF EXISTS fraud1")
sql ='''CREATE TABLE fraud1(
bank VARCHAR
(30),
card_type VARCHAR
(20),
timer VARCHAR
(30),
date VARCHAR
(30),
latitude VARCHAR
(30),
longitude VARCHAR
(30),
device_token VARCHAR
(200),
phone VARCHAR
(30),
type_of_transaction VARCHAR
(30),
i_d VARCHAR
(30)
)'''
cursor.execute(sql)
conn.commit()
print("fraud1 table created successfully")
cursor.execute("DROP TABLE IF EXISTS fraudcheque")
sql ='''CREATE TABLE fraudcheque(
cheque_no VARCHAR
(20),
date_of_cheque VARCHAR
(20),
amount VARCHAR(20),
phone VARCHAR(20),
pay_to VARCHAR(20),
ble_mac_id VARCHAR(20),
device_id VARCHAR(200)
)'''
cursor.execute(sql)
conn.commit()
print("fraudcheque table created successfully")
cursor.execute("DROP TABLE IF EXISTS image")
sql ='''CREATE TABLE image(
img_path VARCHAR(200),
i_d VARCHAR(23),
phone VARCHAR(30),
date VARCHAR(30)
)'''
cursor.execute(sql)
conn.commit()
print("image table created successfully")
cursor.execute("DROP TABLE IF EXISTS infinicue_master_table")
sql ='''CREATE TABLE infinicue_master_table(
barcodeno VARCHAR(30),
name VARCHAR(30),
lastname VARCHAR(30),
passkey VARCHAR(30),
ble_mac_id VARCHAR(30),
qrcode VARCHAR(30),
device_id VARCHAR(100),
email VARCHAR(30),
device_token VARCHAR(200),
pubkey VARCHAR(2500),
privkey VARCHAR(2500),
key VARCHAR(500),
product VARCHAR(20)
)'''
cursor.execute(sql)
conn.commit()
print("infinicue_master_table created successfully")
cursor.execute("DROP TABLE IF EXISTS infinicue_temporary_table")
sql ='''CREATE TABLE infinicue_temporary_table(
barcodeno VARCHAR(30),
name VARCHAR(30),
lastname VARCHAR(30),
phone VARCHAR(30),
passkey VARCHAR(30),
ble_mac_id VARCHAR(30),
qrcode VARCHAR(30),
device_id VARCHAR(100),
email VARCHAR(20),
device_token VARCHAR(200),
pubkey VARCHAR(2500),
privkey VARCHAR(2500),
key VARCHAR(500),
product VARCHAR(20)
)'''
cursor.execute(sql)
conn.commit()
print("infinicue_temporary_table created successfully")
cursor.execute("DROP TABLE IF EXISTS insurance_card")
sql ='''CREATE TABLE insurance_card(
phone VARCHAR(30),
card_type VARCHAR(30),
username VARCHAR(30),
s_no VARCHAR(30),
company VARCHAR(30),
uuid VARCHAR(30),
card_no VARCHAR(30)
)'''
cursor.execute(sql)
conn.commit()
print("insurance_card table created successfully")
cursor.execute("DROP TABLE IF EXISTS insurance_card_event")
sql ='''CREATE TABLE insurance_card_event(
ble_mac_id VARCHAR(30),
device_id VARCHAR(30),
card_type VARCHAR(30),
card_no VARCHAR(30),
username VARCHAR(30),
uuid VARCHAR(30),
s_no VARCHAR(30),
event_type VARCHAR(30),
latitude VARCHAR(30),
longitude VARCHAR(30),
timer VARCHAR(300),
time VARCHAR(30),
date VARCHAR(30),
i_d VARCHAR(30),
phone VARCHAR(30)
)'''
cursor.execute(sql)
conn.commit()
print("insurance_card_event table created successfully")
cursor.execute("DROP TABLE IF EXISTS online_banking")
sql ='''CREATE TABLE online_banking(
cardnumber VARCHAR(30),
name VARCHAR(30),
phone VARCHAR(30),
cvv VARCHAR(30)
)'''
cursor.execute(sql)
conn.commit()
print("online_banking table created successfully")
cursor.execute("DROP TABLE IF EXISTS passkey")
sql ='''CREATE TABLE passkey(
passkey VARCHAR(30),
barcodeno VARCHAR(30)
)'''
cursor.execute(sql)
conn.commit()
print("passkey table created successfully")
cursor.execute("DROP TABLE IF EXISTS passport_detail")
sql ='''CREATE TABLE passport_detail(
name VARCHAR(30),
lastname VARCHAR(30), 
email VARCHAR(30),
phone VARCHAR(30)
)'''
cursor.execute(sql)
conn.commit()
print("passport_detail table created successfully")
cursor.execute("DROP TABLE IF EXISTS private")
sql ='''CREATE TABLE private(
barcodeno VARCHAR(30),
phone VARCHAR(30),
device_id VARCHAR(100),
privkey VARCHAR(2500),
pubkey VARCHAR(2500)
)'''
cursor.execute(sql)
conn.commit()
print("private table created successfully")
cursor.execute("DROP TABLE IF EXISTS qrcode")
sql ='''CREATE TABLE qrcode(
qrcode VARCHAR(30),
ble_mac_id VARCHAR(30),
barcodeno VARCHAR(30),
version VARCHAR(30),
type VARCHAR(30)
)'''
cursor.execute(sql)
conn.commit()
print("qrcode table created successfully")
cursor.execute("DROP TABLE IF EXISTS random")
sql ='''CREATE TABLE random(
passkey VARCHAR(30),
randompasskey VARCHAR(30),
id VARCHAR(30)
)'''
cursor.execute(sql)
conn.commit()
print("random table created successfully")
cursor.execute("DROP TABLE IF EXISTS retailer_user")
sql ='''CREATE TABLE retailer_user(
name VARCHAR(30),
phone VARCHAR(30),
email VARCHAR(30),
barcodeno VARCHAR(30)
)'''
cursor.execute(sql)
conn.commit()
print("retailer_user table created successfully")
cursor.execute("DROP TABLE IF EXISTS share_table")
sql ='''CREATE TABLE share_table(
bank VARCHAR(30),
card_type VARCHAR(30),
phone VARCHAR(30),
share_phone VARCHAR(30),
s_no VARCHAR(30),
card_name VARCHAR(30),
uuid VARCHAR(30)
)'''
cursor.execute(sql)
conn.commit()
print("share_table table created successfully")
cursor.execute("DROP TABLE IF EXISTS timer_table")
sql ='''CREATE TABLE timer_table(
ble_mac_id VARCHAR(30),
timer VARCHAR(30),
card_type VARCHAR(30),
phone VARCHAR(30),
bank_name VARCHAR(30),
latitude VARCHAR(30),
longitude VARCHAR(30),
s_no VARCHAR(30),
date VARCHAR(30),
device_id VARCHAR(300),
card_name VARCHAR(30),
share VARCHAR(30),
type_of_transaction VARCHAR(30),
device_token VARCHAR(300),
count INT,
i_d VARCHAR(30)
)'''
cursor.execute(sql)
conn.commit()
print("timer_table table created successfully")
cursor.execute("DROP TABLE IF EXISTS userdata")
sql ='''CREATE TABLE userdata(
name VARCHAR(30),
phone VARCHAR(30),
email VARCHAR(30),
barcodeno VARCHAR(30),
qrcode VARCHAR(30)
)'''
cursor.execute(sql)
conn.commit()
print("userdata table created successfully")
cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS Receivedcard")
sql ='''CREATE TABLE Receivedcard(
bank VARCHAR(30),
card_type VARCHAR(30),
phone VARCHAR(30),
s_no VARCHAR(30),
share_no VARCHAR(20),
card_name VARCHAR(30)
)'''
cursor.execute(sql)
conn.commit()
print("Receivedcard table created successfully")
  
cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS Income")
sql ='''CREATE TABLE Income(
  id SERIAL,
   salary INT
,
   business INT
,  Phone VARCHAR,
commission INT,
   total_income INT
,
   monthyear VARCHAR
(20)
   )'''
cursor.execute(sql)
conn.commit()
print(" Income Table created successfully........")
cursor = conn.cursor()
cursor.execute('insert into Income(salary,business,commission,total_income,monthyear,phone) values (%s,%s,%s,%s,%s,%s)',[0,0,0,0,'0','0'])
conn.commit()
# #Closing the connection

cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS CardDetail")
sql ='''CREATE TABLE CardDetail(
  id VARCHAR
(30),
   bank VARCHAR
(30),
   card_type VARCHAR
(30),
   account_type VARCHAR
(30),
   phone VARCHAR
(30),
   name VARCHAR
(30),
   card_name VARCHAR
(20),
   url VARCHAR(100)
   )'''
cursor.execute(sql)
conn.commit()
print(" CardDetail Table created successfully........")


cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS Bank")
sql ='''CREATE TABLE Bank(
   
   id SERIAL,
   Phone VARCHAR (30),
   saving_bank_name VARCHAR
(30),
   saving_bank_amount INT

   )'''
cursor.execute(sql)
conn.commit()
print(" Bank Table created successfully........")
cursor = conn.cursor()
cursor.execute('insert into Bank(saving_bank_name,saving_bank_amount,Phone) values (%s,%s,%s)',['synd',400,'8867614097'])
conn.commit()
# #Closing the connection


cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS FD")
sql ='''CREATE TABLE FD(
  id SERIAL,
  Phone VARCHAR
,
  fd_bank_name VARCHAR
(30),
   fd_from_date VARCHAR
(30),
   fd_to_date VARCHAR
(30),
  fd_amount INT
,
  fd_no_of_months INT
,
  fd_no_of_years INT

   )'''
cursor.execute(sql)
conn.commit()
print(" FD Table created successfully........")
cursor = conn.cursor()
cursor.execute('insert into FD(fd_bank_name,fd_from_date,fd_to_date,fd_amount,fd_no_of_months,fd_no_of_years,phone) values (%s,%s,%s,%s,%s,%s,%s)',['','','',0,0,0,'0'])
conn.commit()
# #Closing the connection


cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS RD")
sql ='''CREATE TABLE RD(
  id SERIAL,
  Phone VARCHAR
,
  rd_bank_name VARCHAR
(30),
   rd_from_date VARCHAR
(30),
   rd_to_date VARCHAR
(30),
  rd_amount INT
,
  rd_no_of_months INT
,
  rd_no_of_years INT

   )'''
cursor.execute(sql)
conn.commit()
print(" RD Table created successfully........")
cursor = conn.cursor()
cursor.execute('insert into RD(rd_bank_name,rd_from_date,rd_to_date,rd_amount,rd_no_of_months,rd_no_of_years,Phone) values (%s,%s,%s,%s,%s,%s,%s)',['','','',0,0,0,'0'])
conn.commit()
# #Closing the connection

cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS History")
sql ='''CREATE TABLE History(
   
  id SERIAL,
  Phone VARCHAR
,
  long VARCHAR
(30),
   lat VARCHAR
(30),
   time1 VARCHAR
(30),
  date1 VARCHAR
(30),
  category VARCHAR
(30),
  address VARCHAR
(300),
  monthyear VARCHAR
(30)
   )'''
cursor.execute(sql)
conn.commit()
print(" History Table created successfully........")
# #Closing the connection

cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS In_Bud_Exp_Bal")
sql ='''CREATE TABLE In_Bud_Exp_Bal(
   
  id SERIAL,
  Phone VARCHAR
,
  income INT
,
   budget INT   
,
   expense INT
,
   balance INT
,
   monthyear VARCHAR
(20)
   )'''
cursor.execute(sql)
conn.commit()
print(" In_Bud_Exp_Bal Table created successfully........")
cursor = conn.cursor()
cursor.execute('insert into In_Bud_Exp_Bal(income,budget,expense,balance,monthyear,Phone) values (%s,%s,%s,%s,%s,%s)',[0,0,0,0,'0','0'])
conn.commit()
# #Closing the connection

cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS Fixed_Spends")
sql ='''CREATE TABLE Fixed_Spends(
   
  id SERIAL,
  Phone VARCHAR
,
   fixed_spends_date Date,
   grocery INT
,
   fuel INT
,
   rent INT
,
   vegetables INT
,
   dairyproducts INT
,
   electricity_bill INT
,
   cable_bill INT
,
   water_bill INT
,
   newsPaper INT
,
   fitness INT
,
   lpg INT
,
   house_maid INT
,
   phonebill INT
,
   broadband INT
,
   fixed_spends_total INT
,
   monthyear VARCHAR (30),
   groceryexp INT
,
   fuelexp INT
,
   rentexp INT
,
   vegetablesexp INT
,
   dairyproductsexp INT
,
   electricity_billexp INT
,
   cable_billexp INT
,
   water_billexp INT
,
   newsPaperexp INT
,
   fitnessexp INT
,
   lpgexp INT
,
   house_maidexp INT
,
   phonebillexp INT
,
   broadbandexp INT

   )'''
cursor.execute(sql)
conn.commit()
print(" Fixed_Spends Table created successfully........")
cursor = conn.cursor()
#cursor.execute('insert into fixed_Spends() values (%s,%s,%s,%s,%s)',[0,0,0,0,'0'])
conn.commit()
#Closing the connection


cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS Variable_Spends")
sql ='''CREATE TABLE Variable_Spends(
   
  id SERIAL,
  Phone VARCHAR
,
  variable_spends_date VARCHAR
(30),
   fruits INT
,
   metro INT
,
   bus INT
,
   auto INT
,
   cab INT
,
   medicines INT
,
   ironing INT
,
   stationary INT
,
   repairs INT
,
   saloon INT
,
   parlour INT
,
   medical_checkup INT
,
   Total_variable_spends INT
,
   monthyear VARCHAR
(30),
   fruitsexp INT
,
   metroexp INT
,
   busexp INT
,
   autoexp INT
,
   cabexp INT
,
   medicinesexp INT
,
   ironingexp INT
,
   stationaryexp INT
,
   repairsexp INT
,
   saloonexp INT
,
   parlourexp INT
,
   medical_checkupexp INT

   )'''
cursor.execute(sql)
conn.commit()
print(" Variable_Spends Table created successfully........")
cursor = conn.cursor()
#cursor.execute('insert into fixed_Spends() values (%s,%s,%s,%s,%s)',[0,0,0,0,'0'])
conn.commit()


cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS Contingency")
sql ='''CREATE TABLE Contingency(
   
   id SERIAL,
   Phone VARCHAR
,
   contingency_spends_date VARCHAR
(30),
   education INT
,
   medical INT
,
   marriage INT
,
   Total_contingency_spends INT
,
   monthyear VARCHAR
(30),
   educationexp INT
,
   medicalexp INT
,
   marriageexp INT

   )'''
cursor.execute(sql)
conn.commit()
print(" Contingency Table created successfully........")
cursor = conn.cursor()
#cursor.execute('insert into fixed_Spends() values (%s,%s,%s,%s,%s)',[0,0,0,0,'0'])
conn.commit()


cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS Contingency")
sql ='''CREATE TABLE Contingency(
   
   id SERIAL,
   Phone VARCHAR
,
   contingency_spends_date VARCHAR
(30),
   education INT
,
   medical INT
,
   marriage INT
,
   Total_contingency_spends INT
,
   monthyear VARCHAR
(30),
   educationexp INT
,
   medicalexp INT
,
   marriageexp INT

   )'''
cursor.execute(sql)
conn.commit()
print(" Contingency Table created successfully........")
cursor = conn.cursor()
#cursor.execute('insert into fixed_Spends() values (%s,%s,%s,%s,%s)',[0,0,0,0,'0'])
conn.commit()


cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS Last_location")
sql ='''CREATE TABLE Last_location(
   
  id SERIAL,
  Phone VARCHAR
,
  long VARCHAR
(30),
   lat VARCHAR
(30),
   time1 VARCHAR
(30),
  date1 VARCHAR
(30),
  address VARCHAR
(300)
   )'''
cursor.execute(sql)
conn.commit()
print(" Last_location Table created successfully........")
# #Closing the connection




cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS CardEventApp")
sql ='''CREATE TABLE CardEventApp(
   
  id SERIAL,
  Phone VARCHAR
,
  longitude VARCHAR
(30),
   lattitude VARCHAR
(30),
   time1 VARCHAR
(30),
  date1 VARCHAR
(30),
  address VARCHAR
(300),
  count INT,
  bankname VARCHAR(30),
  cardtype VARCHAR(30),
  category VARCHAR(30),
  macid VARCHAR(30),

  sno VARCHAR(10),
  amount INT,
  monthyear VARCHAR(30),
  currencysymbol VARCHAR(30),
  verifytime VARCHAR(30),
  cardname VARCHAR(30)
 )'''
cursor.execute(sql)
conn.commit()
print(" CardEvent Table created successfully........")
# #Closing the connection


cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS CashEventApp")
sql ='''CREATE TABLE CashEventApp(
   
  id SERIAL,
  Phone VARCHAR
,
  longitude VARCHAR
(30),
   lattitude VARCHAR
(30),
   time1 VARCHAR
(30),
  date1 VARCHAR
(30),
  address VARCHAR
(300),
  count INT,
  category VARCHAR(30),
  amount INT,
  monthyear VARCHAR(30)
   )'''
cursor.execute(sql)
conn.commit()
print("CashEvent Table created successfully........")
# #Closing the connection


cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS NetBanking")
sql ='''CREATE TABLE NetBanking(
   
  id SERIAL,
  Phone VARCHAR
,
  longitude VARCHAR
(30),
   lattitude VARCHAR
(30),
   time1 VARCHAR
(30),
  date1 VARCHAR
(30),
  address VARCHAR
(300),
  count INT,
  category VARCHAR(30),
  amount INT,
  monthyear VARCHAR(30)
   )'''
cursor.execute(sql)
conn.commit()
print("NetBanking Table created successfully........")
# #Closing the connection

cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS UPIEvent")
sql ='''CREATE TABLE UPIEvent(
   
  id SERIAL,
  Phone VARCHAR
,
  longitude VARCHAR
(30),
   lattitude VARCHAR
(30),
   time1 VARCHAR
(30),
  date1 VARCHAR
(30),
  address VARCHAR
(300),
  count INT,
  category VARCHAR(30),
  amount INT,
  monthyear VARCHAR(30),
  receiver_phone VARCHAR(20),
  receiver_bank VARCHAR(20)

   )'''
cursor.execute(sql)
conn.commit()
print("CashEvent Table created successfully........")


cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS Online")
sql ='''CREATE TABLE Online(
   
  id SERIAL,
  Phone VARCHAR
,
  longitude VARCHAR
(30),
   lattitude VARCHAR
(30),
   time1 VARCHAR
(30),
  date1 VARCHAR
(30),
  address VARCHAR
(300),
  count INT,
  category VARCHAR(30),
  amount INT,
  monthyear VARCHAR(30)
   )'''
cursor.execute(sql)
conn.commit()
print("Online Table created successfully........")

cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS ChequeEvent")
sql ='''CREATE TABLE ChequeEvent(
   
  id SERIAL,
  Phone VARCHAR
,
  longitude VARCHAR
(30),
   lattitude VARCHAR
(30),
   time1 VARCHAR
(30),
  date1 VARCHAR
(30),
  address VARCHAR
(300),
  count INT,
  category VARCHAR(30),
  amount INT,
  monthyear VARCHAR(30),
  date_of_cheque VARCHAR(30),
  cheque_no VARCHAR(30),
  pay_to Varchar(30)

   )'''
cursor.execute(sql)
conn.commit()
print("Cheque Table created successfully........")

cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS ClosedUser")
sql ='''CREATE TABLE ClosedUser(
   
  id SERIAL,
  Ownerphone VARCHAR(20)
,
  Sharenumber VARCHAR(20)

   )'''
cursor.execute(sql)
conn.commit()
print(" ClosedUser Table created successfully........")

cursor.execute("DROP TABLE IF EXISTS BankApi")
sql ='''CREATE TABLE BankApi(
   
  id SERIAL,
  BankName VARCHAR(20)
,
  API VARCHAR(200)

   )'''
cursor.execute(sql)
conn.commit()
print(" BankApi Table created successfully........")


cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS MerchantRepo")
sql ='''CREATE TABLE MerchantRepo(
   QR_Code_Data VARCHAR
(30) NOT NULL,
   phone VARCHAR(20)
 
   )'''
cursor.execute(sql)
conn.commit()
print(" MerchantRepo Table created successfully........")
# #Closing the connection


cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS Netbankdata")
sql ='''CREATE TABLE Netbankdata(
   username VARCHAR
(30) NOT NULL,
   phone VARCHAR(20),
   password VARCHAR(20)
   )'''
cursor.execute(sql)
conn.commit()
print(" Netbankdata Table created successfully........")
# #Closing the connection

cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS Onlinebank")
sql ='''CREATE TABLE Onlinebank(
   cardnumber VARCHAR
(30) NOT NULL,
   phone VARCHAR(20),
   expiry VARCHAR(20),
   cvv VARCHAR(3)
   )'''
cursor.execute(sql)
conn.commit()
print(" Onlinebank Table created successfully........")
# #Closing the connection

cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS Adhaardata")
sql ='''CREATE TABLE Adhaardata(
   adhaar VARCHAR
(30) NOT NULL,
   phone VARCHAR(20)
   )'''
cursor.execute(sql)
conn.commit()
print(" Adhaar Table created successfully........")
cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS Emids")
sql ='''CREATE TABLE Emids(
   Hospital VARCHAR
(30) NOT NULL,
   Lattitude VARCHAR(20),
   Longitude VARCHAR(20),
   Phone VARCHAR(20)
   )'''
cursor.execute(sql)
conn.commit()
print(" Emids Table created successfully........")
cursor.execute("DROP TABLE IF EXISTS BankName")
sql ='''CREATE TABLE BankName(
   BankName VARCHAR
(30) NOT NULL,
   CardType VARCHAR(20),
   CardName VARCHAR(20),
   AccountType VARCHAR(30)
   )'''
cursor.execute(sql)
conn.commit()
print(" BankName Table created successfully........")

cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS Passport_Event")
sql ='''CREATE TABLE Passport_Event(
   
  id SERIAL,
  Phone VARCHAR
,
  longitude VARCHAR
(30),
   lattitude VARCHAR
(30),
   time1 VARCHAR
(30),
  date1 VARCHAR
(30),
  address VARCHAR
(300),
  monthyear VARCHAR(30)
   )'''
cursor.execute(sql)
conn.commit()
print("Passport_Event Table created successfully........")
# #Closing the connection
