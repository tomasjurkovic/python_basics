# lists:
print([2, 4, 6] == [2, 4, 6])  # they are same = True
print([2, 4, 6] == [6, 4, 2])  # they are not same = False

# dictionaries:
first = {0: 2.7, 1: 4.4, 3: 7.0001, 4: 8.47}
second = {3: 7.0001, 0: 2.7, 1: 4.4, 4: 8.47}
print(first == second)  # prints True because their orders do not matter -> the key value pairs matter
