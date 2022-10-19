console = {"nintendo": "wii", "microsoft": "xbox", "sony": "playstation"}
# there are key value pairs, they must be separated by comas and spaces.

# I can access them same as I would use index number
print(console["microsoft"])

# I can assign them to variables:
example_var = console["sony"]
print(example_var)

# or it can be used in expressions
print("I have bought " + console["microsoft"] + " One some time ago.")

# other examples of dictionaries:
hardest = {9: "corundum", 10: "diamond"}
floats = {1.23: 100, 1.445: 1000, 1.7897: 10000}
mixed = {"string": 1, 10210: 2, 4.975: 3, False: 4}

# of course we can do the same with these dictionaries:
print(mixed[False])
print(floats[1.445])
print(hardest[9])
