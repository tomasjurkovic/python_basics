num_list = [50, 2.5964, 0, -99, 55, 100, 6, 3.21]
# sorting makes this list from smallest to biggest one:
num_list.sort()
print(num_list)  # prints [-99, 0, 2.5964, 3.21, 6, 50, 55, 100]

num_list.sort(reverse=True) # with this argument added it prints values from biggest to smallest
print(num_list)  # prints [100, 55, 50, 6, 3.21, 2.5964, 0, -99]

str_list = ["Ringo", "John", "George", "Paul"]
print(str_list)
str_list.sort()  # it works also for strings
print(str_list)  # prints ["George", "John", "Paul", "Ringo"]
str_list.sort(reverse=True)  # also available for strings
print(str_list)  # prints ["Ringo", "Paul", "John", "George"]

# we cannot use sort method if there are multiple data types in the list
mixed = [2, False, "mixed not", 3.22]

# but if there are no strings in the list, we can sort it:
mixed_without_strings = [False, 5.668, -9]
mixed_without_strings.sort()
print(mixed_without_strings)  # prints [-9, False, 5.668] because False value = 0

# ASCIIbetical order is applied in string sorting:
ASSCIIbetical = ["Boris", "Andrew", "apple", "banana"]
ASSCIIbetical.sort()
print(ASSCIIbetical)  # prints ['Andrew', 'Boris', 'apple', 'banana']

# we can use key=str.lower to make it sort in alphabetical order
ASSCIIbetical.sort(key=str.lower)
print(ASSCIIbetical)  # now it prints ['Andrew', 'apple', 'banana', 'Boris'] in alphabetical order

