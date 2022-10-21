set_1 = {1, 2, 3, 4, 5}
set_2 = {6, 7, 8, 9, 10}

# we use intersection function to find out what have two sets in common
set_3 = set_1.intersection(set_2)
print(set_3)  # in this case nothing, so just set() is printed

# let's create new set:
set_4 = {1, 3, 5, 7, 9}
set_5 = set_1.intersection(set_4)
print(set_5)  # in this case {1, 3, 5} is printed, because both sets contain these values

# this does the same as above:
set_6 = set_2 & set_4
print(set_6)  # {7, 9} is printed
