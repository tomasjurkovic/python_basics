player_numbers = {1: "Aaron", 2: "Kieran", 3: "Benjamin", 5: "Thomas", 6: "Gabriel", 7: "Bukayo"}

print(player_numbers.items())
# prints dict_items([(1, 'Aaron'), (2, 'Kieran'), (3, 'Benjamin'), (5, 'Thomas'), (6, 'Gabriel'), (7, 'Bukayo')])

for item in player_numbers.items():
    print(item)

# prints:
# (1, 'Aaron')
# (2, 'Kieran')
# (3, 'Benjamin')
# (5, 'Thomas')
# (6, 'Gabriel')
# (7, 'Bukayo')

# better looking:
for key, value in player_numbers.items():
    print(key, value)

# prints:
# 1 Aaron
# 2 Kieran
# 3 Benjamin
# 5 Thomas
# 6 Gabriel
# 7 Bukayo