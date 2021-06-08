import requests, json
from tkinter import *
from tkinter.ttk import Combobox

def open_auth_page(screen):
    print("Scrren")
    window = Frame(screen, width=800, height=600, bg="#ffffab")
    window.place(x=50, y=50)
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

    LoginBtn = Button(window, bg="#61f25a", fg="white", font=("Gotham", "15"), text="Login", width=30)
    LoginBtn.place(x=10, y=280)


def open_calc_page(screen):

    window = Frame(screen, width=800, height=600)
    window.place(x=50, y=50)

    def cliked():
        inp1 = input1.get()
        inp2 = input2.get()
        math1 = combobox.get()
        result = 0

        # if type(inp1) is str or type(inp2) is str:
        #    return print("введите числовое значение")
        # else:
        if math1 == "+":
            result = int(inp1) + int(inp2)
            print(result)
        elif math1 == "-":
            result = int(inp1) - int(inp2)
            print(result)
        elif math1 == "*":
            result = int(inp1) * int(inp2)
            print(result)
        elif math1 == "/":
            result = int(inp1) / int(inp2)
            print(result)
        else:
            "не верный расчет"

        result1.config(text=result)

    input1 = Entry(window, bg="orange", fg="red", width=10, font=20)
    input1.grid(column=0, row=0
                )
    input2 = Entry(window, bg="blue", fg="red", width=10, font=20)
    input2.grid(column=2, row=0, padx=5, pady=3)

    result1 = Label(window, bg="white", fg="red", text="", width=20, font=20)
    result1.grid(column=3, row=0, padx=5, pady=3)

    btn = Button(window, bg="yellow", text="Расчет", command=cliked)
    btn.grid(column=2, row=1)

    combobox = Combobox(window)
    combobox["values"] = ("+", "-", "/", "*")
    combobox.current(0)
    combobox.grid(column=1, row=0)
