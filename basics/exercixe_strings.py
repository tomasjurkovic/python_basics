text = "Just do it!"
# printing "!"
print(text[10:])

# printing "do"
print(text[5:7])

# printing "it!"
print(text[8:])

# printing "Just"
print(text[:4])

text2 = "Don't"

# printing "Don't do it" by slicing first string and concatenating it with another string
print(text2 + " " + text[5:])
