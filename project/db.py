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
        return data


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
        cursor.execute("SELECT f.*, g.title as genre_title FROM film as f INNER JOIN genre as g ON f.genre_id == g.id")
        data = cursor.fetchall()
        print(data)
        return data

    def get_films_by_genre(self, id):
        cursor = self.connection.cursor()
        cursor.execute(f"SELECT f.*, g.title as genre_title FROM film as f INNER JOIN genre as g ON f.genre_id == g.id WHERE f.genre_id = {id}")
        data = cursor.fetchall()
        print(data)
        return data

class User:
    def __init__(self, path):
        self.connection = create_connection(path)

    def create_table(self):
        cursor = self.connection.cursor()
        cursor.execute("""
        CREATE TABLE user(
            id INTEGER primary key,
            firstname VARCHAR(50),
            lastname VARCHAR(50),
            username VARCHAR(50) UNIQUE,
            email VARCHAR(100) UNIQUE,
            password VARCHAR(50)
        );
        """)
        print("TABLE user CREATED")

    def registration(self, firstname, lastname, username, email, password):

        cursor = self.connection.cursor()
        sql = '''INSERT INTO user(firstname, lastname, username, email, password) VALUES(?, ?, ?, ?, ?);'''
        cursor.execute(sql, [firstname, lastname, username, email, password])
        self.connection.commit()
        print("VALUES INSERTED")

    def login(self, username, password):
        cursor = self.connection.cursor()
        cursor.execute(f"SELECT * FROM user WHERE(username=='{username}' and password == '{password}')")
        data = cursor.fetchall()
        return data