text = input("Write some text here and program will calculate number of characters in it: ")

count = 0

for letter in text:
    count += 1


print("You entered this string: " + str(text))
print("The number of characters in string is: " + str(count))
