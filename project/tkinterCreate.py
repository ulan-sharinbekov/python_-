from tkinter import *
from db_init import genresTable, films, tupleGenres, genre_map, convertToBinaryData
from tkinter.ttk import Combobox
from tkinter import filedialog

filepath = ""

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

    def back():
        display.destroy()

    def create():
        title = entTitle.get()
        desc = entDesc.get()
        rating = int(entRating.get())
        genre_id = genre_map[ComboGenre.get()]
        photo_path = filepath
        blob = convertToBinaryData(photo_path)
        films.create_film(title, desc, rating, genre_id, blob)


    def UploadAction(event=None):
        global filepath
        filename = filedialog.askopenfilename()
        filepath = filename



    display = Frame(window, height=700, width=1300, bg="GREEN")
    display.place(x=0, y=0)

    back = Button(display, text="back", font=("Gotham", "15"), command=back)
    back.place(x=20, y=10)

    lblTitle = Label(display, text="Title", font=("Gotham", "15"))
    lblTitle.place(x=150, y=100)

    entTitle = Entry(display, font=("Gotham", "15"))
    entTitle.place(x=250, y=100)

    lblDesc = Label(display, text="Description", font=("Gotham", "15"))
    lblDesc.place(x=150, y=160)

    entDesc = Entry(display, font=("Gotham", "15"))
    entDesc.place(x=250, y=160)

    lblRating = Label(display, text="Rating", font=("Gotham", "15"))
    lblRating.place(x=150, y=220)

    entRating = Entry(display, font=("Gotham", "15"))
    entRating.place(x=250, y=220)

    lblGenre = Label(display, text="Genre", font=("Gotham", "15"))
    lblGenre.place(x=150, y=280)

    ComboGenre = Combobox(display, font=("Gotham", "15"))
    ComboGenre['values'] = tuple(tupleGenres)
    ComboGenre.current(1)
    ComboGenre.place(x=250, y=280)

    lblPhoto = Label(display, text="Photo", font=("Gotham", "15"))
    lblPhoto.place(x=150, y=340)

    # entPhoto = Entry(display, font=("Gotham", "15"))
    # entPhoto.place(x=250, y=340)
    btnFile = Button(display, text="File", font=("Gotham", "15"), command=UploadAction)
    btnFile.place(x=250, y=340)

    btn = Button(display, text="Create", font=("Gotham", "15"), command=create)
    btn.place(x=200, y=400)
