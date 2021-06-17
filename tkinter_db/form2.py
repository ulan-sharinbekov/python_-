from tkinter import *
from db_class import Profile

window = Tk()
window.geometry("500x500")
path = "Profiles.sql"

x = 0
y = 0

profiles = Profile(path)
data = profiles.get_all_profiles()

for profile in data:
    profile = list(profile)
    lbl = Label(window, text=str(profile[0]) + " " + profile[1] + " " + profile[2]+ " " + profile[3] + " " + profile[4])
    lbl.place(x=10, y=y+40)
    y=y+40

window.mainloop()