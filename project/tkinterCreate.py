from tkinter import *
from db_init import genresTable, films


def create_genre_page(window):

    def back():
        display.destroy()

    def createGenre():
        title = entTitle.get()
        desc = entDesc.get()
        if title and desc:
            genresTable.create_genre(title, desc)
        else:
            pass

    display = Frame(window, height=700, width=1300, bg="GREEN")
    display.place(x=0, y=0)

    back = Button(display, text="back", font=("Gotham", "15"), command=back)
    back.place(x=20, y=10)

    lblTitle = Label(window, text="Title", font=("Gotham", "15"))
    lblTitle.place(x=150, y=100)

    entTitle = Entry(window, font=("Gotham", "15"))
    entTitle.place(x=250, y=100)

    lblDesc = Label(window, text="Description", font=("Gotham", "15"))
    lblDesc.place(x=150, y=160)

    entDesc = Entry(window, font=("Gotham", "15"))
    entDesc.place(x=250, y=160)

    btn = Button(window, text="Create",  font=("Gotham", "15"), command=createGenre)
    btn.place(x=200, y=220)

def create_film_page(window):
    pass