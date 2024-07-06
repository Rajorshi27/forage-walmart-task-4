import csv
import sqlite3

def create_tables(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS shipping_data_0 (
            origin_warehouse TEXT,
            destination_store TEXT,
            product TEXT,
            on_time TEXT,
            product_quantity INTEGER,
            driver_identifier TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS shipping_data_1 (
            shipment_identifier TEXT,
            product TEXT,
            on_time TEXT,
            origin_warehouse TEXT,
            destination_store TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS shipping_data_2 (
            shipment_identifier TEXT,
            origin_warehouse TEXT,
            destination_store TEXT,
            driver_identifier TEXT
        )
    """)

def insert_shipping_data_0(cursor):
    with open('/workspace/forage-walmart-task-4/data/shipping_data_0.csv', 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for row in csv_reader:
            origin_warehouse, destination_store, product, on_time, product_quantity, driver_identifier = row
            cursor.execute("INSERT INTO shipping_data_0 (origin_warehouse, destination_store, product, on_time, product_quantity, driver_identifier) VALUES (?, ?, ?, ?, ?, ?)",
                           (origin_warehouse, destination_store, product, on_time, product_quantity, driver_identifier))

def insert_shipping_data_1(cursor):
    with open('/workspace/forage-walmart-task-4/data/shipping_data_1.csv', 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for row in csv_reader:
            shipment_identifier, product, on_time = row
            cursor.execute("INSERT INTO shipping_data_1 (shipment_identifier, product, on_time) VALUES (?, ?, ?)",
                           (shipment_identifier, product, on_time))

def insert_shipping_data_2(cursor):
    with open('/workspace/forage-walmart-task-4/data/shipping_data_2.csv', 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for row in csv_reader:
            shipment_identifier, origin_warehouse, destination_store, driver_identifier = row
            cursor.execute("INSERT INTO shipping_data_2 (shipment_identifier, origin_warehouse, destination_store, driver_identifier) VALUES (?, ?, ?, ?)",
                           (shipment_identifier, origin_warehouse, destination_store, driver_identifier))

if __name__ == "__main__":
    conn = sqlite3.connect('/workspace/forage-walmart-task-4/shipment_database.db')
    cursor = conn.cursor()

    create_tables(cursor)  # Create the necessary tables

    insert_shipping_data_0(cursor)
    insert_shipping_data_2(cursor)
    insert_shipping_data_1(cursor)  # Insert into shipping_data_1

    conn.commit()
    conn.close()
