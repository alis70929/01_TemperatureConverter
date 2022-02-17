from csv import field_size_limit
from fileinput import filename
import re
from urllib.request import DataHandler
data = ["I", 'love', "computers"]

has_error = "yes"
while has_error == "yes":
    has_error = "no"
    filename = input("Enter a filename (leave off extension): ")

    valid_char = "[A-za-z0-9_]"
    for letter in filename:
        if re.match(valid_char, filename):
            continue

        elif letter == " ":
            problem = "no spaces allowed"
        else:
            problem = "no {}'s allowed".format(letter)
        has_error = "yes"
    if filename == "":
        problem = "can't be blank"
        has_error = "yes"
    
    if has_error == "yes":
        print("Invalid filename - {}".format(problem))
    else:
        print("you entered a valid filename")

filename = filename + ".txt"

f = open(filename, "w+")

for item in data:
    f.write(item + "\n")

f.close()