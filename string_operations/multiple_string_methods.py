print("TEXT".lower().isupper())
# it returns False, because we lowered it

print("Batman".isalpha())
# prints True, because it contains only letters

print("nbs123".isalnum())
print("300".isalnum())
print("Arsenal".isalnum())
# returns True, because it contains only letters and/or numbers

print("10".isnumeric()) # or .isdecimal()
# prints True because it contains only numbers
print("10.1".isnumeric()) # or .isdecimal()
# prints False because it contains numbers and special character

print(" ".isspace())
print("              ".isspace())
# prints True because it contains only empty characters
print("Not just spaces".isspace()) # prints False
print("Not just spaces"[3].isspace()) # prints True, because the 3rd index is really empty space

print("The Empire Strikes Back".istitle()) # yes it is, because first letters are capital
print("Sumer Smash Brothers: Ultimate!".istitle()) # yes it is as well, it can contains even special characters

print("the great gatsby".title()) # it makes string title case - The Great Gatsby
