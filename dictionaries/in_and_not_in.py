dict_one = {0: 100, 1: 444, 2: 647, 3: 363}

# in operator:
print(3 in dict_one)  # prints True, because 3 key exists in dict_one dictionary
print(7 in dict_one)  # prints False, because 7 key does not exist in dict_one dictionary

# not in operator:
print(3 not in dict_one)  # prints False, because 3 key exists in dict_one dictionary
print(7 not in dict_one)  # prints True, because 7 key does not exist in dict_one dictionary

# this is how we use it in values:
player_numbers = {1: "Aaron", 2: "Kieran", 3: "Benjamin", 5: "Thomas", 6: "Gabriel", 7: "Bukayo"}
print("Gabriel" in player_numbers.values())
# prints True, because this value is there
