indexes_example = ["carpet", "hardwood", "linoleum"]
print(indexes_example[1])
# it prints 'second' item in list => hardwood

indexes_example_2 = [[1, 11, 111], [2, 3, 4], [70, 80, 99]]
print(indexes_example_2[2][2])
# it prints 99, because I selected third item in the third list of indexes_example_2

print(indexes_example[2][2])
# it prints 'n', because I we print third character in third item of the string in the list

negative = [1, 2, 2, 4, 5]
print(negative[-1])
# 5 is printed because I use negative indexing which starts from -1 and it prints final value in the list
# print(negative[-10]) - it would be out of list
print(negative[-4]) # it prints 2

mixed = [False, 365, 3.15, "this is a string"]
print(mixed[2] + 1.85)  # prints 5 because we can apply addition there.
print("I have used \"" + mixed[-1] + "\" as an example too many times")
# prints 'I have used "this is a string" as an example too many times'
