checked_list = [1, 2, 3, 4]
print(1 in checked_list)  # it checks if 1 is in this list and prints True
print(9 in checked_list)  # it checks if 9 is in this list and prints False

# it can be assigned to variables
not_in_example = 8 not in checked_list
# when printed, it returns True because it is not there
print(not_in_example)

actually_in_example = 3 not in checked_list
# it returns False value
print(actually_in_example)