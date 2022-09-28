def write_file(filename="", text=""):
 """function that appends a string at the end of a text"""
with open(filename, mode="w", encoding="UTF-8") as f:
    return f.write(text)

