from sqlite3 import *


def create_connection(path):
    connection = None
    try:
        connection = connect(path, check_same_thread=False)
        print("Connection is successful")
    except Error as e:
        print(e)
    return connection

class Product:
    def __init__(self, path):
        self.connection = create_connection(path)

    def create_table(self):
        TABLE_PRODUCT = """
        CREATE TABLE products(
            ID VARCHAR(40) UNIQUE,
            name VARCHAR(40),
            amount INT,
            price INT,
            category VARCHAR(40)
        )
        """
        cursor = self.connection.cursor()
        cursor.execute(TABLE_PRODUCT)
        print("TABLE Product created")

    def insert_product(self, id, name, amount, price, category):
        cursor = self.connection.cursor()
        cursor.execute(f"INSERT INTO products VALUES({id}, '{name}', {amount}, {price}, '{category}')")
        self.connection.commit()
        print("data inserted")

    def select_products(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM products")
        data = cursor.fetchall()
        print(data)
        return data
