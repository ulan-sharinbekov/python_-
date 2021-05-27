a = {
    "data": "table",
    "after": "ta"
}
dict1 = {
    "data": "table"
}
if list(a.keys()).count("before"):
    dict1.update(a)

print(dict1)