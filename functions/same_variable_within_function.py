example = "Hello world"
# global

# variable used within the function is not the same variable declared in the same file that is not within the function


def loc_ex():
    example = "this is completely different variable"
    # local
    return example


# one variable can't be local and global variable at the same time
print(example)
print(loc_ex())
