from tkinter import *
from PIL import ImageTk, Image
from db_init import write_file, genresTable, films

def film_window(window, film_table):

    def back():
        display.destroy()

    def open_genre_page():
        genre_window(window, genresTable)

    display = Frame(window, height = 700, width=1300)
    display.place(x=0, y=0)
    baseX = 100
    baseY = 100

    back = Button(display, text="back", font=("Gotham", "15"), command=back)
    back.place(x=20, y=10)

    genres = Button(display, text="genres", font=("Gotham", "15"), command=open_genre_page)
    genres.place(x=100, y=10)

    def show_film(x, y, id, name, descr, rating, genre_id, photo, genre_title):
        namelbl = Label(display, text=name, font=("Gotham", "12"))
        namelbl.place(x=x+230, y=y+10)

        descrlbl = Label(display, text=descr, font=("Gotham", "12"))
        descrlbl.place(x=x + 230, y=y+60)

        ratinglbl = Label(display, text=rating, font=("Gotham", "12"))
        ratinglbl.place(x=x + 700, y=y+10)

        genrelbl = Label(display, text=genre_title, font=("Gotham", "12"))
        genrelbl.place(x=x + 230, y=y+200)

        write_file(photo, name + ".jpg")
        image1 = Image.open(name + ".jpg")
        image1 = image1.resize((180, 240), Image.ANTIALIAS)
        test = ImageTk.PhotoImage(image1)
        label1 = Label(display, image=test, width=180, height=240)
        label1.image = test
        label1.place(x=x+10, y=y)

    films = film_table.get_films()
    for film in films:
        id = film[0]
        name = film[1]
        descr = film[2]
        rating = film[3]
        genre_id = film[4]
        photo = film[5]
        genre_title = film[6]
        show_film(baseX, baseY, id, name, descr, rating, genre_id, photo, genre_title)
        baseY+=300


def genre_window(window, genre_table):
    def back():
        display.destroy()

    display = Frame(window, height = 700, width=1300)
    display.place(x=0, y=0)
    baseX = 100
    baseY = 100

    back = Button(display, text="back", font=("Gotham", "15"), command=back)
    back.place(x=20, y=10)

    def show_genre(x, y, id, name, descr):

        def get_films_by_genre():
            filmslist = films.get_films_by_genre(id)
            filmlist_window(window, filmslist)
        idlbl = Label(display, text=str(id), font=("Gotham", "12"))
        idlbl.place(x=x + 90, y=y + 10)

        namelbl = Label(display, text=name, font=("Gotham", "12"))
        namelbl.place(x=x+110, y=y+10)

        descrlbl = Label(display, text=descr, font=("Gotham", "12"))
        descrlbl.place(x=x + 100, y=y+30)

        line = Canvas(display, width=1000, height=2, bg="BLUE")
        line.place(x=x, y=y + 50)

        films_genre = Button(display, text="films", command=get_films_by_genre)
        films_genre.place(x=x+700, y=y+10)

    genres = genre_table.get_genres()
    print(genres)
    for genre in genres:
        id = genre[0]
        name = genre[1]
        descr = genre[2]

        show_genre(baseX, baseY, id, name, descr)
        baseY+=60

def filmlist_window(window, filmlist):
    def back():
        display.destroy()

    def open_genre_page():
        genre_window(window, genresTable)

    display = Frame(window, height = 700, width=1300)
    display.place(x=0, y=0)
    baseX = 100
    baseY = 100

    back = Button(display, text="back", font=("Gotham", "15"), command=back)
    back.place(x=20, y=10)

    genres = Button(display, text="genres", font=("Gotham", "15"), command=open_genre_page)
    genres.place(x=100, y=10)

    def show_film(x, y, id, name, descr, rating, genre_id, photo, genre_title):
        namelbl = Label(display, text=name, font=("Gotham", "12"))
        namelbl.place(x=x+230, y=y+10)

        descrlbl = Label(display, text=descr, font=("Gotham", "12"))
        descrlbl.place(x=x + 230, y=y+60)

        ratinglbl = Label(display, text=rating, font=("Gotham", "12"))
        ratinglbl.place(x=x + 700, y=y+10)

        genrelbl = Label(display, text=genre_title, font=("Gotham", "12"))
        genrelbl.place(x=x + 230, y=y+200)

        write_file(photo, name + ".jpg")
        image1 = Image.open(name + ".jpg")
        image1 = image1.resize((180, 240), Image.ANTIALIAS)
        test = ImageTk.PhotoImage(image1)
        label1 = Label(display, image=test, width=180, height=240)
        label1.image = test
        label1.place(x=x+10, y=y)

    films = filmlist
    for film in films:
        id = film[0]
        name = film[1]
        descr = film[2]
        rating = film[3]
        genre_id = film[4]
        photo = film[5]
        genre_title = film[6]
        show_film(baseX, baseY, id, name, descr, rating, genre_id, photo, genre_title)
        baseY+=300
