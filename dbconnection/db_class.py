from sqlite3 import *


def create_connection(path):
    connection = None
    try:
        connection = connect(path)
        print("Connection is successful")
    except Error as e:
        print(e)
    return connection

class Car:
    def __init__(self, path):
        self.connection = create_connection(path)

    def create_table(self):
        TABLE_CARS = """
        CREATE TABLE car(
            ID INT,
            brand VARCHAR(40),
            model VARCHAR(40),
            _year INT
        )
        """
        cursor = self.connection.cursor()
        cursor.execute(TABLE_CARS)
        print("TABLE CAR created")

    def insert_car(self, id, model, brand, year):
        cursor = self.connection.cursor()
        cursor.execute(f"INSERT INTO car VALUES({id}, '{brand}', '{model}', {year})")
        self.connection.commit()
        print("data inserted")

    def select_car(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM car")
        data = cursor.fetchall()
        print(data)
