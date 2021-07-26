from db import Genre, Film, User, Comment

path = "kinopoisk.sql"


def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData

def write_file(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') as file:
        file.write(data)


genresTable = Genre(path)
films = Film(path)
users = User(path)
commentTable = Comment(path)


tupleGenres = []
genre_map = {}
listGenres = genresTable.get_genres()
for i in listGenres:
    genre_map[i[1]] = i[0]
    tupleGenres.append(i[1])
