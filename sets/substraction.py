set_1 = {4, 5, 6, 7, 8}
set_2 = {6, 7, 8, 9, 10}

# subtraction just removes what both sets have in common and
# only that what is unique in first set, that remains
# results are different if we change the order:

set_3 = set_1 - set_2
print(set_3)  # prints {4, 5}

set_4 = set_2 - set_1
print(set_4)  # prints {9, 10}

# other way how to do the same thing:
set_5 = set_1.difference(set_2)
set_6 = set_2.difference(set_1)
print(set_5)  # prints {4, 5}
print(set_6)  # prints {9, 10}
