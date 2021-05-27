import json
f = open("task1.json", "r")

row = f.read()
dict1 = json.loads(row)

print(type(dict1))
print(dict1["Student"]["name"])
# print(dict1.Student.name)

