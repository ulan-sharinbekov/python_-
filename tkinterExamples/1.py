from tkinter import *
from tkinter.ttk import Combobox, Checkbutton

def cliked():
    some_text = input1.get()
    txt2.config(text = some_text)

window = Tk()
window.geometry('800x600')
window.title("Welcome to new window")

txt = Label(window, bg="green", fg="black", width=30, text="это виджет Label")
txt.pack()
txt2 = Label(window, bg="blue", fg="white", width=30, text="это виджет Label 2 ")
txt2.pack()

input1 = Entry(window, bg="orange", fg="red", width=30, font=20)
input1.pack()

btn = Button(window, bg="yellow", text="Click", command = cliked)
btn.pack()

combobox = Combobox(window)
combobox['values'] = (1,2,3,4,5,'Текст1','Текст2')
combobox.current(1)
combobox.pack()


check = Checkbutton(window, text="Выбор")
check.pack()

window.mainloop()
