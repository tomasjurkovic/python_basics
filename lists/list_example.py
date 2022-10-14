# Create a variable
# and assign it a list that contains an integer, a float, a Boolean value, a string, and a list of 3 integers.
example_list = [100, 3.14, True, "Super", [3, 2, 1]]

# Create another variable and assign it a call of the list() function with a string as its argument.
another_list = list("example")

# Use the keyword "in" to check
# if the letter "e" is in the list assigned to the variable from step 2 and print the result.
print("e" in another_list)  # prints True, because it is there

# Use the keyword "not in" to check
# if the letter "a" is not in the list assigned to the variable from step 2 and print the result.
print("a" not in another_list)  # prints False, because it is there
