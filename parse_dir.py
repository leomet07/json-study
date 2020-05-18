from parse_img import parse_img
import os
import sys
import json


def merge_two_dicts(x, y):
    """Given two dicts, merge them into a new dict as a shallow copy."""
    z = x.copy()
    z.update(y)
    return z


words = {}
for r, d, f in os.walk("imgs"):
    for file in f:

        texture_path = os.path.join(r, file)

        words_returned = parse_img(texture_path, False)

        words = merge_two_dicts(words, words_returned)

        print(
            "Finished "
            + file
            + " with "
            + str(len(words_returned.keys()))
            + " defintions."
        )
        # print(words_returned)

        print("\n\n")


print(words)
print("Total definitions is: " + str(len(words.keys())))

with open("file.json", "w", encoding="utf-8") as f:
    json.dump({"words": words}, f, ensure_ascii=False, indent=4)
