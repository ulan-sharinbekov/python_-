import requests, json
from tkinter import *
from module2 import open_auth_page, open_calc_page


def open_auth():
    open_auth_page(window)

def open_calc():
    open_calc_page(window)


window = Tk()
window.geometry("1000x700")

btn1 = Button(text="auth", command=open_auth)
btn1.pack()
btn2 = Button(text="calc", command=open_calc)
btn2.pack()




window.mainloop()
