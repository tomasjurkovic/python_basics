ints = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(ints[::4])  # prints stride length of 4 (1, 5, 9)
print(ints[1::2])  # prints evens only (2, 4, 6, 8, 10)
print(ints[8::-1])  # prints backwards (9, 8, 7, 6, 5, 4, 3, 2, 1)
print(ints[8::-2])  # prints odds backwards: (9, 6, 3)

# [number1:number2:number3]
# number 1 = from
# number 2 = to
# number 3 = by how much + goes up - goes down

print(ints[1:6:2])  # prints (2, 4, 6)

