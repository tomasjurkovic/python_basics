tuple_1 = ("a", "b", "c", "d", "e")
tuple_2 = (2.784, False, [1, 2, 3])
tuple_3 = (1, 0, 1, 1, 0)
# this is how we create tuple

# but can do it also by tuple function:
tuple_4 = tuple([3.14, 2.205, 10])
tuple_5 = tuple("edcba")

# the list was turned into tuple directly:
print(tuple_4)  # prints (3.14, 2.205, 10)
# the string was divided into characters that created tuple:
print(tuple_5)  # prints ('e', 'd', 'c', 'b', 'a')
