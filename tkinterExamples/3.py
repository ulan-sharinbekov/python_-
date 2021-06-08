from tkinter import *
from tkinter.ttk import Combobox, Checkbutton

window = Tk()
window.geometry('800x600')
window.title("Welcome to new window")

txt = Label(window, bg="green", fg="black", width=30, text="0 0")
txt.place(x=0, y=0)
txt2 = Label(window, bg="blue", fg="white", width=30, text="1 0 ")
txt2.place(x=20, y=30)
# txt = Label(window, bg="red", fg="white", width=30, text="0 1")
# txt.grid(column=0, row=1)
# txt2 = Label(window, bg="yellow", fg="black", width=30, text="1 1")
# txt2.grid(column=1, row=1)

window.mainloop()
