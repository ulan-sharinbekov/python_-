from db import fk_on
from tkinter import *
from tkinterUser import reg_window, log_window
from db_init import users

fk_on()

window = Tk()
window.geometry("1300x700")

def login():
    log_window(window, users)

def registr():
    reg_window(window, users)

log = Button(window, text="Log In", command=login)
log.place(x=300, y=400)
reg = Button(window, text="Sign Up", command=registr)
reg.place(x=600, y=400)


window.mainloop()




# img = convertToBinaryData("mech.jpg")
# print(img)
# # films.create_table()
# films.create_film("Механик ", "Джейсон Стэйтем мстит за лучшего друга",
#                     6, 2,  img )
# data = films.get_films()
# img = data[1][5]
# write_file(img, "img.jpg")
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

