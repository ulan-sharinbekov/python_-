import json

f = open("json1.json", "r")

row = f.read()
f.close()
data = json.loads(row)  # str -> dict

print(type(data))
print(data["name"])

data["name"] = "Bagjan"

f1 = open("json1.json", "w")

ans = json.dumps(data) # dict -> str
f1.write(ans)