from tkinter import *

def film_window(window, film_table):

    display = Frame(window, height = 700, width=1000)
    display.place(x=0, y=0)
    baseX = 100
    baseY = 100

    def show_film(x, y, id, name, descr, rating, genre_id, photo):
        namelbl = Label(display, text=name, font=("Gotham", "12"))
        namelbl.place(x=x+10, y=y)

        descrlbl = Label(display, text=descr, font=("Gotham", "12"))
        descrlbl.place(x=x + 10, y=y+20)

        ratinglbl = Label(display, text=rating, font=("Gotham", "12"))
        ratinglbl.place(x=x + 100, y=y)

        genrelbl = Label(display, text=genre_id, font=("Gotham", "12"))
        genrelbl.place(x=x + 120, y=y)




    films = film_table.get_films()
    for film in films:
        id = film[0]
        name = film[1]
        descr = film[2]
        rating = film[3]
        genre_id = film[4]
        photo = film[5]
        show_film(baseX, baseY, id, name, descr, rating, genre_id, photo)
        baseY+=60

