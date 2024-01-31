import psycopg2
from psycopg2 import OperationalError

def create_table():
    try:
        # Establish a connection to the PostgreSQL database
        connection = psycopg2.connect(
            user="postgres",
            password="0000",
            host="localhost",
            port="5432",
            database="infinicue"
        )

        # Create a cursor object using the cursor() method
        cursor = connection.cursor()

        # SQL statement to create the data_entry table
        create_table_query = '''CREATE TABLE IF NOT EXISTS data_entry (
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
