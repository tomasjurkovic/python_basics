nested = (1, 2, 3, (4, 5, 6), (7, 8, 9), (10, "there can be strings as well", 12))
print(nested[4])  # prints (7, 8, 9)
print(nested[5][1])  # prints "there can be strings as well"
print(nested[4][2])  # prints 9

# count method:
repeat = (1, 0, 2, 0, 3, 0, 1, 5, 0, 1, 1, 0)
print(repeat.count(7))  # prints 0
print(repeat.count(0))  # prints 5
print(repeat.count(1))  # prints 4
print(repeat.count(5))  # prints 1

# index method:
print(repeat.index(1))  # prints 0, because the first time it is located on 0 index
print(repeat.index(5))  # prints 7, because it is present only once on 7 index
print(repeat.index(0))  # prints 1, because the first time it is located on 1 index
# print(repeat.index(10))  # it would return error - ValueError: tuple.index(x): x not in tuple
