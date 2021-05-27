import json

f = open("task1.json", "r")

row = f.read()
f.close()
data = json.loads(row)  # str -> dict

print(type(data))
print(data["Wednesday"])

data["Wednesday"].append("Algebra")

f1 = open("task1.json", "w")

ans = json.dumps(data)  # dict -> str
f1.write(ans)