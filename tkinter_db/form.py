from tkinter import *
from db_class import Profile

window = Tk()
window.geometry("500x500")
path = "Profiles.sql"


def signup():
    profile = Profile(path)
    firstname = entryname.get()
    surename = entrysurename.get()
    email = entryemail.get()
    password = entrypass.get()
    new_ID = profile.get_count_of_profiles() + 1

    profile.registration(new_ID, firstname, surename, email, password)
    # profile.create_table()
    profile.get_all_profiles()


label1 = Label(window, text="Registrtion")
label1.place(x=175, y=10)

labelname = Label(window, text="Firstname: ")
labelname.place(x=20, y=40)

entryname = Entry(window)
entryname.place(x=300, y=40)

lblsurename = Label(window, text="Surename: ")
lblsurename.place(x=20, y=80)

entrysurename = Entry(window)
entrysurename.place(x=300, y=80)

labelemail = Label(window, text="Email: ")
labelemail.place(x=20, y=120)

entryemail = Entry(window)
entryemail.place(x=300, y=120)

lblpass = Label(window, text="Password: ")
lblpass.place(x=20, y=160)

entrypass = Entry(window)
entrypass.place(x=300, y=160)

btn = Button(window, text="Create", command=signup)
btn.place(x=175, y=200)

window.mainloop()