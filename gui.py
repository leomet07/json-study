from __future__ import print_function
import os
import sys
import json
import tkinter as tk
from tkinter.filedialog import asksaveasfile


master = tk.Tk()

master.title("Defintion maker")


master.geometry("600x600")

listbox = tk.Listbox(master)
listbox.pack()
# display words
data = {"words": {}}


def display_file(file):
    if not (os.path.exists(file)):
        loaded = {"words": {}}

    else:
        with open(file) as json_file:
            loaded = json.load(json_file)

    print(loaded)

    if not (type(loaded) is dict):
        loaded = {}

    if not ("words" in loaded):
        loaded["words"] = {}
    c = 0
    for key in data["words"]:
        listbox.delete(c)
        c += 1

    data["words"] = loaded["words"]
    keys = list(data["words"].keys())

    # clear listbox
    # get the data

    for item in keys:
        listbox.insert(tk.END, str(item) + " : " + str(data["words"][item]))


name_label = tk.Label(master, text="The words name",)
name_label.pack()
name_form = tk.Entry(master)
name_form.pack()


def_label = tk.Label(master, text="The word's definition",)
def_label.pack()
def_form = tk.Entry(master)
def_form.pack()

look_dir = ""

first_click = True


def clicked():
    name = name_form.get()
    definition = def_form.get()

    if name == "" or definition == "":
        return ""

    global first_click
    if first_click:

        get_file()

    print(
        "Button Clicked with a word of "
        + str(name)
        + " and a defintion of "
        + str(definition)
    )

    data["words"][name] = definition

    listbox.insert(tk.END, str(name) + " : " + str(definition))
    print("saving to " + str(os.path.join(look_dir, "file.json")))
    with open(os.path.join(look_dir, "file.json"), "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    first_click = False


def get_file():
    global first_click
    global look_dir
    look_dir = tk.filedialog.askdirectory()
    print(look_dir)
    file_path = os.path.join(look_dir, "file.json")

    display_file(file_path)

    first_click = False


btn = tk.Button(master, text="Submit", command=clicked)
# btn.grid(column=1, row=0)
btn.pack()


name_label = tk.Label(
    master,
    text='Select directory to save the "file.json" to, and to look for a previous defintion list in',
)
name_label.pack()


get_file_btn = tk.Button(master, text="Select dir", command=get_file)
# btn.grid(column=1, row=0)
get_file_btn.pack()
# -----------


tk.mainloop()
