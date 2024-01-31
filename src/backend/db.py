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
        create_table_query = '''CREATE TABLE IF NOT EXISTS data_entry (
            id SERIAL PRIMARY KEY,
            barcodeno VARCHAR(255),
            wallet_type VARCHAR(255),
            walletcolor VARCHAR(255),
            manufacturingdate DATE,
            batchnum VARCHAR(255),
            countrycode VARCHAR(255),
            qrcode VARCHAR(255),
            blemacid VARCHAR(255),
            version VARCHAR(255),
            barcode_location VARCHAR(255),
            qrcode_location VARCHAR(255)
        )'''

        # Execute the CREATE TABLE command
        cursor.execute(create_table_query)
        connection.commit()
        print("Table created successfully!")

    except OperationalError as e:
        print(f"The error '{e}' occurred.")

    finally:
        # Close the cursor and connection
        if connection:
            cursor.close()
            connection.close()

# Call the function to create the table
create_table()
