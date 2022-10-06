# the_string = input("Please insert some sentence: \n")
#
# new_string = ""
# index = len(the_string) - 1
#
# for letter in the_string:
#     if the_string[index].isalnum() or the_string[index].isspace() or the_string[index] == "-" or the_string[index] == "'" or index >= 0:
#         new_string += letter
#         index -= 1
#     else:
#         new_string += ""
#         index -= 1
#
# words = new_string.split()
# number_of_word = len(words)
# print(words)
# print(number_of_word)


the_string = input("Please insert some sentence: \n")

new_string = ""

for char in the_string:
    if char.isalnum() or char.isspace() or char == "-" or char == "'":
        new_string += char

words = new_string.split()
number_of_word = len(words)
print(words)
print(number_of_word)