# solution I did
the_string = input("Insert some string: \n")
index = len(the_string) - 1
new_string = ""

for letter in the_string:
    new_string += the_string[index]
    index -= 1

# it will print reversed string according to inserted characters
print(new_string)

# solution from udemy:
user_string = input("Please enter a string.")
reversed = ""

for item in range(len(user_string) - 1, -1, -1):
    reversed += user_string[item]

print(reversed)
