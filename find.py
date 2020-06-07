import json

data = {}
with open("file.json") as json_file:
    data = json.load(json_file)

data = data["words"]
keys = list(data.keys())

# print(keys)


search = input("search for? ")
res = [i for i in keys if (i.lower()).startswith(search.lower())]
print(res)
output = []
for i in res:
    output.append(data[i])
print(output)


dicticnary = {}
for i in range(0, len(output)):
    defi = output[i]
    word = res[i]

    dicticnary[word] = defi

print(dicticnary)


wait = input("Wating")
