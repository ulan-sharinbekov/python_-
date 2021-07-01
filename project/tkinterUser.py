from tkinter import *


def reg_window(window, user_table):
    def back():
        display.destroy()
    def reg():
        fn = firstnameent.get()
        ln = lastnameent.get()
        un = usernameent.get()
        ps = passwordent.get()
        em = emailent.get()

        if fn and ln and un and ps and em:
            errlbl.config(text="OK", fg="GREEN")
            try:
                user_table.registration(fn, ln, un, em, ps)

            except:
                errlbl.config(text="User email or username must be unique", fg="RED")
        else:
            errlbl.config(text="ALL FIELDS ARE REQUIRED", fg="RED")




    display = Frame(window, height=700, width=1000)
    display.place(x=0, y=0)


    back = Button(display, text="back", font=("Gotham", "15"), command=back)
    back.place(x=20, y=10)

    title = Label(display, text="Registration", font=("Gotham", "15"))
    title.place(x=450, y=10)

    firstnamelbl = Label(display, text="Firstname", font=("Gotham", "15"))
    firstnamelbl.place(x=300, y=60)

    firstnameent = Entry(display, font=("Gotham", "15"))
    firstnameent.place(x=550, y=60)

    lastnamelbl = Label(display, text="Lastname", font=("Gotham", "15"))
    lastnamelbl.place(x=300, y=100)

    lastnameent = Entry(display, font=("Gotham", "15"))
    lastnameent.place(x=550, y=100)

    usernamelbl = Label(display, text="Username", font=("Gotham", "15"))
    usernamelbl.place(x=300, y=140)

    usernameent = Entry(display, font=("Gotham", "15"))
    usernameent.place(x=550, y=140)

    passwordlbl = Label(display, text="Password", font=("Gotham", "15"))
    passwordlbl.place(x=300, y=180)

    passwordent = Entry(display, font=("Gotham", "15"), show ="*")
    passwordent.place(x=550, y=180)

    emaillbl = Label(display, text="Email", font=("Gotham", "15"))
    emaillbl.place(x=300, y=220)

    emailent = Entry(display, font=("Gotham", "15"))
    emailent.place(x=550, y=220)

    btn = Button(display, text="Sign Up", command = reg, font=("Gotham", "15"))
    btn.place(x=475, y = 260)

    errlbl = Label(display, text="", font=("Gotham", "10"))
    errlbl.place(x = 475, y = 300)


def log_window(window, user_table):
    def back():
        display.destroy()
    def log():
        un = usernameent.get()
        ps = passwordent.get()

        if un and ps:

            user = user_table.login(un, ps)
            if user:
                errlbl.config(text="OK", fg="GREEN")
            else:
                errlbl.config(text="User doesn't exist", fg="RED")
        else:
            errlbl.config(text="ALL FIELDS ARE REQUIRED", fg="RED")

    display = Frame(window, height=700, width=1000)
    display.place(x=0, y=0)

    back = Button(display, text="back", font=("Gotham", "15"), command=back)
    back.place(x=20, y=10)

    title = Label(display, text="Login", font=("Gotham", "15"))
    title.place(x=450, y=10)

    usernamelbl = Label(display, text="Username", font=("Gotham", "15"))
    usernamelbl.place(x=300, y=60)

    usernameent = Entry(display, font=("Gotham", "15"))
    usernameent.place(x=550, y=60)

    passwordlbl = Label(display, text="Password", font=("Gotham", "15"))
    passwordlbl.place(x=300, y=100)

    passwordent = Entry(display, font=("Gotham", "15"))
    passwordent.place(x=550, y=100)

    btn = Button(display, text="Log In", command=log, font=("Gotham", "15"))
    btn.place(x=475, y=140)

    errlbl = Label(display, text="", font=("Gotham", "10"))
    errlbl.place(x=475, y=200)