#!/bin/python3

"""function that inserts a line of text to a file"""

def append_after(filename="", search_string="", new_string=""):
    with open(filename, mode="r", encoding="UTF-8") as f:
        my_text = f.readline()
       
   with open(filename, mode="w") as x:
 text = " " 
for line in x:
        text += line
    if search_string in line:
       text += new_string
  
    x.write(text)
