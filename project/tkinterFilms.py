from tkinter import *
from PIL import ImageTk, Image
from db_init import write_file, genresTable, films, commentTable
from tkinterCreate import create_genre_page, create_film_page
import json
from datetime import date as date_module, datetime

def film_window(window, film_table, offset):

    def back():
        display.destroy()

    def open_genre_page():
        genre_window(window, genresTable)

    def open_next():
        film_window(window, film_table, offset+2)

    def open_prev():
        b = max(0, offset-2)
        film_window(window,film_table, b)

    def create_genre():
        create_genre_page(window)

    def create_film():
        create_film_page(window)

    display = Frame(window, height = 700, width=1300, bg="GREEN")
    display.place(x=0, y=0)
    baseX = 100
    baseY = 100

    back = Button(display, text="back", font=("Gotham", "15"), command=back)
    back.place(x=20, y=10)

    genres = Button(display, text="genres", font=("Gotham", "15"), command=open_genre_page)
    genres.place(x=100, y=10)

    createGenre = Button(display, text="Create Genre", font=("Gotham", "15"), command=create_genre)
    createGenre.place(x=200, y=10)

    createFilm = Button(display, text="Create Film", font=("Gotham", "15"), command=create_film)
    createFilm.place(x=400, y=10)

    # сделать prevPage

    prevPage = Button(display, text="prev", font=("Gotham", "15"), command=open_prev)
    prevPage.place(x=450, y=600)

    nextPage = Button(display, text="next", font=("Gotham", "15"), command=open_next)
    nextPage.place(x=1000, y=600)

    def show_film(x, y, id, name, descr, rating, genre_id, photo, genre_title):

        def open_film_onclick(event):
            exact_film(window, id)

        namelbl = Label(display, text=name, font=("Gotham", "12"))
        namelbl.place(x=x+230, y=y+10)
        namelbl.bind('<Button-1>', open_film_onclick)

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

    films = film_table.get_films(offset)
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
            filmslist = films.get_films_by_genre(id, 0)
            filmlist_window(window, filmslist, id, 0)
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

def filmlist_window(window, filmlist, genre_id, offset):
    def back():
        display.destroy()

    def open_genre_page():
        genre_window(window, genresTable)

    def open_prev():
        global films
        b = max(0, offset-2)
        filmsList = films.get_films_by_genre(genre_id, b)
        filmlist_window(window, filmsList, genre_id, b)

    def open_next():
        global films
        filmsList = films.get_films_by_genre(genre_id, offset+2 )
        filmlist_window(window, filmsList, genre_id, offset+2)

    display = Frame(window, height = 700, width=1300)
    display.place(x=0, y=0)
    baseX = 100
    baseY = 100

    back = Button(display, text="back", font=("Gotham", "15"), command=back)
    back.place(x=20, y=10)

    genres = Button(display, text="genres", font=("Gotham", "15"), command=open_genre_page)
    genres.place(x=100, y=10)

    # сделать prevPage
    prevPage = Button(display, text="prev", font=("Gotham", "15"), command=open_prev)
    prevPage.place(x=450, y=600)

    nextPage = Button(display, text="next", font=("Gotham", "15"), command=open_next)
    nextPage.place(x=1000, y=600)

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

def exact_film(window, id):

    def back():
        display.destroy()

    def open_genre_page():
        genre_window(window, genresTable)

    def show_comment(x,y,comment_id, user_id, film_id, content, date, username):
        usernamelbl = Label(display, text=username, font=("Gotham", "12"))
        usernamelbl.place(x=x + 230, y=y + 200)

        contentlbl = Label(display, text=content, font=("Gotham", "12"))
        contentlbl.place(x=x + 230, y=y + 240)

        datelbl = Label(display, text=date, font=("Gotham", "12"))
        datelbl.place(x=x + 900, y=y + 200)

    def create_comment():
        content = entComment.get()
        f = open("localstorage.json", "r")
        row = f.read()
        data = json.loads(row)

        today = date_module.today()
        now = datetime.now().time()  # time object
        d1 = today.strftime("%d/%m/%Y")
        d1 = str(d1)
        now = str(now)

        commentTable.create_comment(data["user_id"], id, content, d1+" "+now )


    display = Frame(window, height = 700, width=1300, bg="GREEN")
    display.place(x=0, y=0)
    baseX = 100
    baseY = 100

    back = Button(display, text="back", font=("Gotham", "15"), command=back)
    back.place(x=20, y=10)

    genres = Button(display, text="genres", font=("Gotham", "15"), command=open_genre_page)
    genres.place(x=100, y=10)

    film = films.get_exact_film(id)
    name = film[1]
    descr = film[2]
    rating = film[3]
    genre_id = film[4]
    photo = film[5]
    genre_title = film[6]

    namelbl = Label(display, text=name, font=("Gotham", "12"))
    namelbl.place(x=330, y=110)

    descrlbl = Label(display, text=descr, font=("Gotham", "12"))
    descrlbl.place(x=330, y=160)

    ratinglbl = Label(display, text=rating, font=("Gotham", "12"))
    ratinglbl.place(x=800, y=110)

    genrelbl = Label(display, text=genre_title, font=("Gotham", "12"))
    genrelbl.place(x=1000, y=110)

    write_file(photo, name + ".jpg")
    image1 = Image.open(name + ".jpg")
    image1 = image1.resize((180, 240), Image.ANTIALIAS)
    test = ImageTk.PhotoImage(image1)
    label1 = Label(display, image=test, width=180, height=240)
    label1.image = test
    label1.place(x=110, y=100)


    entComment = Entry(display, font=("Gotham", "12"), width=50)
    entComment.place(x=330, y=200)

    btnCreate = Button(display, text="Create", font=("Gotham", "12"), command=create_comment)
    btnCreate.place(x=800, y=200)

    comments = commentTable.get_film_comment(id)
    for comment in comments:
        comment_id = comment[0]
        user_id = comment[1]
        film_id = comment[2]
        content = comment[3]
        date = comment[4]
        username = comment[5]
        show_comment(baseX, baseY, comment_id, user_id, film_id, content, date, username)
        baseY=baseY+80

