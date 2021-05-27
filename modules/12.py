import calendar

a = calendar.LocaleHTMLCalendar(locale='Russian_Russia')
with open('calendar.html', 'w') as g:
    print(a.formatyear(2021, width=10), file=g)

with open("text.txt", "r") as f:
    print(f.read())
