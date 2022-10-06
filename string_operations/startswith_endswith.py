print("This is a text".startswith("This")) # prints True, because it really starts with 'This'
print("This is a text".startswith("T")) # yes it does
print("This is a text".startswith('t')) # no, it is case-sensitive

print("To infinity and beyond!".endswith("beyond!")) # prints True
print("To infinity and beyond!".endswith("beyond")) # prints False, becasue we missed '!' last character
