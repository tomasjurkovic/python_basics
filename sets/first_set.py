# sets cannot have duplicate values
# sets contain values that are unordered

set_1 = {9, 8, 7, 6}  # set can be created directly
set_2 = set({"a", "b", "c", "d", "e"})  # or by using set method like this

print(set_1)  # prints randomly ordered values like: {8, 9, 6, 7}
print(set_2)  # prints randomly ordered values like: {'d', 'e', 'b', 'a', 'c'}

# if there are duplicate values in set, each value is added only once, the duplicate values are ignored:
set_of_duplicates = {9, 9, 8, 7, 8, 8, 7, 6, 1}  # set can be created directly
print(set_of_duplicates)  # only five values are printed in random order: {1, 6, 7, 8, 9}

# how to create empty set:
empty_set = set()  # just assign it call of set function with no argument
print(empty_set)

# we can use range function in sets
# for example if we want to add all odds numbers from 1 to 100
odds_set = set(range(1, 100, 2))
print(odds_set)

# set can have items that are different data types:
set_of_different_data_types = {"It is possible", True, 10, 11.2345}
print(set_of_different_data_types)

# this looks weird a bit, but 1 = True and 0 = False and it makes sense if no duplications are possible to store:
set_of_01_truefalse = {True, 1, False, 0}
print(set_of_01_truefalse)  # prints {True False}

set_of_numbers = {1, 8, 12, 44, 785}
# we can use also forloop
for num in set_of_numbers:
    print(num)  # prints 1, 785, 8, 12, 44 in random order

# we can use in and not in function
print(8 in set_of_numbers)  # prints True - because it is there
print(44 not in set_of_numbers)  # prints False - because it is there
