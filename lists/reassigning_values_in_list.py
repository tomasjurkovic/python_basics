list_to_change = [1, 2, 3, 4, 5]
print(list_to_change)

# we are able to change values of items in the list, not like in Java
list_to_change[3] = 1000
print(list_to_change)  # it prints [1, 2, 3, 1000, 5]
# we changed the fourth item in the list

list_to_change_2 = [2, 4, 6, 8, 10]
print(list_to_change_2)

# we can edit multiple values at once using slice technique
list_to_change_2[1:4] = [400, 6000, 80000]  # it updates items on indexes from 1 to 3
print(list_to_change_2)  # it prints [2, 400, 6000, 80000, 10]

# we can add/edit also those index numbers which are not included in the original list
list_to_change_2[4:8] = [111, 222, 333, 444]
print(list_to_change_2)  # it prints [2, 400, 6000, 80000, 111, 222, 333, 444]
