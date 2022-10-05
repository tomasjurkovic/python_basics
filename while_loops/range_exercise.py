one_input = range(5)

for num in one_input:
    print(num)
    # prints from 0 to 4 - 0, 1, 2, 3, 4


# it has its own type - range
print(type(one_input))


two_inputs = range(5, 10)

for number in two_inputs:
    print(number)
    # prints from 5 to 9 - 5, 6, 7, 8, 9


three_inputs = range(1, 20, 3)

for number in three_inputs:
    print(number)
    # prints from 1 to 20 every third number - 1, 4, 7, 10, 13, 16, 19


reversed_three_inputs = range(20, 1, -3)

for number in reversed_three_inputs:
    print(number)
    # prints from 20 to 1 every third number - 20, 17, 14, 11, 8, 5, 2


