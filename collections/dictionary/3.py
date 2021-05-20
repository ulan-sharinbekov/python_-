students = [
    {
        "name": "Azamat",
        "age": 18,
        "gpa": 3.8
    },
    {
        "name": "Alikhan",
        "age": 20,
        "gpa": 3.0
    },
    {
        "name": "Gulim",
        "age": 21,
        "gpa": 3.4
    }
]
# print(students)
gpaavg = 0
for student in students:
    gpaavg += student["gpa"]

print(gpaavg / len(students))