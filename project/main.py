from db import Genre, Cinema, Film, fk_on

def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData

def write_file(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') as file:
        file.write(data)

path = "cinema.sql"
fk_on()
# genres = Genre(path)
# cinemas = Cinema(path)
films = Film(path)

# img = convertToBinaryData("300x450.jpg")
# print(img)
# films.create_table()
# films.create_film("Перевозчик", "Перевозя очередную посылку, Фрэнк вынужден нарушить привычные правила. Джейсон Стэйтем в скоростном роуд-муви",
#                     7, 2,  img )
data = films.get_films()
img = data[0][5]
write_file(img, "img.jpg")
#
# genres.create_table()
#
# genres.create_genre("Action", "Action movies")
# genres.create_genre("Боевик", "example")

# genres.get_genres()

# cinemas.create_table()

# cinemas.create_cinema("Chaplin", "Almaty", 15)
# cinemas.create_cinema("Kinopark", "Almaty", 16)

# cinemas.get_cinemas()

