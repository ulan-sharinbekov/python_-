students = [
    {
        "name": "Derbes",
        "age": 20
    },
    {
        "name": "Dana",
        "age": 19
    },
    {
        "name": "Dias",
        "age": 24
    },
    {
        "name": "Azamat",
        "age": 26
    },
    {
        "name": "Orken",
        "age": 17
    }
]
mn = 1111
student = {}
for i in students:
    if i["age"] < mn:
        mn = i["age"]
        student = i
print(student)