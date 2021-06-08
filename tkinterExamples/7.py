import requests, json
from tkinter import *



window = Tk()
window.geometry("400x400")
title = Label(window, font=("Gotham", "15"), text="Auth Form")
title.place(x=140, y=0)

login = Label(window, font=("Gotham", "12"), text="Login")
login.place(x=120, y=50)

signup = Label(window, font=("Gotham", "12"), text="Sign Up")
signup.place(x=200, y=50)

emaillbl = Label(window, font=("Gotham", "10", "bold"), text="Email")
emaillbl.place(x=10, y=100)

emailent = Entry(window, font=("Gotham", "12", "italic"), width=40)
emailent.place(x=10, y=120)

Passwordllbl = Label(window, font=("Gotham", "10", "bold"), text="Password")
Passwordllbl.place(x=10, y=170)

Passwordent = Entry(window, font=("Gotham", "12", "italic"), width=40)
Passwordent.place(x=10, y=190)

LoginBtn = Button(window, bg="#61f25a", fg="white", font=("Gotham", "15"), text = "Login", width=30)
LoginBtn.place(x=10, y=280)

window.mainloop()
