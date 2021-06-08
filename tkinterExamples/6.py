import requests, json
from tkinter import *

def click1():
    label1 = Label(frame1, text="Frame 1 open")
    label1.pack()

def click2():
    label1 = Label(frame1, text="Frame 2 open")
    label1.pack()


window = Tk()
window.geometry("400x400")


btn1 = Button(window, text="frame1", command=click1)
btn1.pack()

btn2 = Button(window, text="frame2", command=click2)
btn2.pack()

frame1 = Frame(window, bg="blue", width=100, height=100)
frame1.pack()

label3 = Label(frame1, bg="black", fg="white", text="Label 3 in Frame 1")
label3.pack()

window.mainloop()
