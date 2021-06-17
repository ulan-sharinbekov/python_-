from tkinter import ttk
from tkinter import *
from db_class import Profile


window = Tk()
window.geometry("1000x500")
path = "Profiles.sql"


def View():
    profiles = Profile(path)
    data = profiles.get_all_profiles()
    for profile in data:
        print(profile) # it print all records in the database
        tree.insert("", END, values=profile)

tree= ttk.Treeview(window, column=("column1", "column2", "column3", "column4", "column5" ), show='headings')
tree.heading("#1", text="ID")
tree.heading("#2", text="FIRST NAME")
tree.heading("#3", text="SURNAME")
tree.heading("#4", text="EMAIL")
tree.heading("#5", text="PASSWORD")

tree.pack()
b2 = Button(text="view data", command=View)
b2.pack()
window.mainloop()