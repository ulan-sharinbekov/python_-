from sqlite3 import *


def create_connection(path):
    connection = None
    try:
        connection = connect(path, check_same_thread=False)
        print("Connection is successful")
    except Error as e:
        print(e)
    return connection

def fk_on():
    connection = create_connection("cinema.sql")
    cursor = connection.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")

class Genre:
    def __init__(self, path):
        self.connection = create_connection(path)

    def create_table(self):
        cursor = self.connection.cursor()
        cursor.execute("""
        CREATE TABLE genre(
            id INTEGER primary key,
            title VARCHAR(250),
            description VARCHAR(250)
        )
        """)
        print("TABLE genre CREATED")

    def create_genre(self, title, description):
        cursor = self.connection.cursor()
        cursor.execute(f"INSERT INTO genre(title, description) VALUES('{title}', '{description}')")
        self.connection.commit()
        print("VALUES INSERTED")

    def get_genres(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM genre")
        data = cursor.fetchall()
        print(data)


class Cinema:
    def __init__(self, path):
        self.connection = create_connection(path)

    def create_table(self):
        cursor = self.connection.cursor()
        cursor.execute("""
        CREATE TABLE cinema(
            id INTEGER primary key,
            name VARCHAR(250),
            city VARCHAR(250),
            rooms INTEGER
        )
        """)
        print("TABLE cinema CREATED")

    def create_cinema(self, name, city, rooms):
        cursor = self.connection.cursor()
        cursor.execute(f"INSERT INTO cinema(name, city, rooms) VALUES('{name}', '{city}', {rooms})")
        self.connection.commit()
        print("VALUES INSERTED")

    def get_cinemas(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM cinema")
        data = cursor.fetchall()
        print(data)


class Film:
    def __init__(self, path):
        self.connection = create_connection(path)

    def create_table(self):
        cursor = self.connection.cursor()
        cursor.execute("""
        CREATE TABLE film(
            id INTEGER primary key,
            title VARCHAR(250),
            description VARCHAR(250),
            rating INTEGER,
            genre_id INT,
            photo BLOB NOT NULL,
            FOREIGN KEY(genre_id) REFERENCES genre(id)
        )
        """)
        print("TABLE film CREATED")

    def create_film(self, title, description, rating, genre_id, photo):

        cursor = self.connection.cursor()
        sql = '''INSERT INTO film(title, description, rating, genre_id, photo) VALUES(?, ?, ?, ?, ?);'''
        cursor.execute(sql, [title, description, rating, genre_id, Binary(photo)])
        self.connection.commit()
        print("VALUES INSERTED")

    def get_films(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM film")
        data = cursor.fetchall()
        return data