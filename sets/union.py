set_1 = {1, 2, 3, 4, 5}
set_2 = {6, 7, 8, 9, 10}
first_ten = set_1.union(set_2)
print(first_ten)  # prints {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# this does the same as above:
pipe_way = set_1 | set_2
print(pipe_way)  # prints {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
