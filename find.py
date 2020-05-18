import json

data = {}
with open("file.json") as json_file:
    data = json.load(json_file)

data = data["words"]
keys = list(data.keys())

print(keys)


search = "ac"
res = [i for i in keys if (i.lower()).startswith(search.lower())]
print(res)
