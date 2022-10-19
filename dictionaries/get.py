player_numbers = {1: "Aaron", 2: "Kieran", 3: "Benjamin", 5: "Thomas", 6: "Gabriel", 7: "Bukayo"}

if 9 in player_numbers:
    print(player_numbers[9])
else:
    print("9 is not a key in player_numbers.")

# prints 9 is not a key in player_numbers.

if 5 in player_numbers:
    print(player_numbers[5])
else:
    print("5 is not a key in player_numbers.")

# prints Thomas

# we can do this above in just one line of code like this:
print(player_numbers.get(11, "11 is not a key in player_numbers."))
# prints 11 is not a key in player_numbers.
print(player_numbers.get(1, "1 is not a key in player_numbers."))
# prints Aaron
