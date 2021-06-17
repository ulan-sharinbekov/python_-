from sqlite3 import *

def create_connection(path):
    connection = None
    try:
        connection = connect(path)
        print("Connection is successful")
    except Error as e:
        print(e)
    return connection


class Profile:
    def __init__(self, path):
        self.connection = create_connection(path)

    def create_table(self):
        TABLE_CREATE = """
        CREATE TABLE Profile(
            ID INT,
            firstname VARCHAR(40),
            surename VARCHAR(40),
            email VARCHAR(40),
            password VARCHAR(40)
        )
        """
        cursor = self.connection.cursor()
        cursor.execute(TABLE_CREATE)
        print("table created")

    def registration(self, ID, firstname, surename, email, password):
        cursor = self.connection.cursor()
        cursor.execute(f"INSERT INTO Profile VALUES({ID}, '{firstname}', '{surename}', '{email}', '{password}')")
        self.connection.commit()
        print(f"INSERTED VALUES({ID}, '{firstname}', '{surename}', '{email}', '{password}')")


    def get_all_profiles(self):
        cursor = self.connection.cursor()
        cursor.execute(f"SELECT * FROM Profile")
        data = cursor.fetchall()
        print(data)
        return data

    def get_count_of_profiles(self):
        cursor = self.connection.cursor()
        cursor.execute(f"SELECT count(ID) FROM Profile")
        data = cursor.fetchall()
        cnt = list(data[0])
        # print(cnt[0])
        return cnt[0]
