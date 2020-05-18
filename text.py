import json
import os
import sys

data = {}
with open("file.json") as json_file:
    data = json.load(json_file)

print(data)

if not ("words" in data):
    data["words"] = {}


overwrite = "n"
if overwrite.lower() == "y":
    data["words"] = {}

while True:
    key = input("What word do you want to add? ")
    if key == "q":
        break
    value = input("What is its definition? ")
    if value == "q":
        break

    data["words"][key] = value

    print({key: value})
    print(data)

with open("file.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
