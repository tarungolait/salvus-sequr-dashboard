import psycopg2
from psycopg2 import OperationalError

def create_table():
    try:
        # Establish a connection to the PostgreSQL database
        connection = psycopg2.connect(
            user="postgres",
            password="zaynmalik2002",
            host="localhost",
            port="5432",
            database="infinicue"
        )

        # Create a cursor object using the cursor() method
        cursor = connection.cursor()

        # SQL statement to create the data_entry table
        create_table_query_data_entry = '''CREATE TABLE IF NOT EXISTS data_entry (
            id SERIAL PRIMARY KEY,
            category VARCHAR(255),
            type VARCHAR(255),
            color VARCHAR(255),
            macId VARCHAR(255),
            qrCode TEXT,
            barcodeNo VARCHAR(255),
            version VARCHAR(255),
            batchNumber VARCHAR(255),
            countryCode VARCHAR(255),
            manufacturingDate DATE,
            barcode_location TEXT,
            qrcode_location TEXT
        )'''

        # Execute the CREATE TABLE command for data_entry table
        cursor.execute(create_table_query_data_entry)
        print("data_entry Table created successfully!")

        # SQL statement to create the product_details table
        create_table_query_product_details = '''CREATE TABLE IF NOT EXISTS product_details (
            id SERIAL PRIMARY KEY,
            product_category VARCHAR(255) NOT NULL,
            product_type VARCHAR(255) NOT NULL,
            color VARCHAR(255) NOT NULL,
            battery_type VARCHAR(255) NOT NULL,
            ble_make VARCHAR(255) NOT NULL,
            version VARCHAR(255) NOT NULL
        )'''

        # Execute the CREATE TABLE command for product_details table
        cursor.execute(create_table_query_product_details)
        print("product_details Table created successfully!")

        # SQL statement to create the bank_contacts table
        create_table_query_bank_contacts = '''CREATE TABLE IF NOT EXISTS bank_contacts (
            id SERIAL PRIMARY KEY,
            bank_name VARCHAR(255),
            type_of_bank VARCHAR(255),
            address VARCHAR(255),
            city VARCHAR(255),
            country VARCHAR(255),
            customer_care_number VARCHAR(255),
            email_id VARCHAR(255),
            official_website VARCHAR(255)
        )'''

        # Execute the CREATE TABLE command for bank_contacts table
        cursor.execute(create_table_query_bank_contacts)
        print("bank_contacts Table created successfully!")

        # Commit the changes
        connection.commit()

    except OperationalError as e:
        print(f"The error '{e}' occurred.")

    finally:
        # Close the cursor and connection
        if connection:
            cursor.close()
            connection.close()

# Call the function to create the tables
create_table()
