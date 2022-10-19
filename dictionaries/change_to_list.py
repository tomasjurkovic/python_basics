player_numbers = {1: "Aaron", 2: "Kieran", 3: "Benjamin", 5: "Thomas", 6: "Gabriel", 7: "Bukayo"}

print(list(player_numbers.values()))
# this prints ['Aaron', 'Kieran', 'Benjamin', 'Thomas', 'Gabriel', 'Bukayo']

# I can store it in the variable simply
list_of_player_names = list(player_numbers.values())
list_of_player_numbers = list(player_numbers.keys())
list_numbers_and_players = list(player_numbers.items())

print(list_of_player_names)
# this prints ['Aaron', 'Kieran', 'Benjamin', 'Thomas', 'Gabriel', 'Bukayo']
print(list_of_player_numbers)
# this prints [1, 2, 3, 5, 6, 7]
print(list_numbers_and_players)
# this prints # [(1, 'Aaron'), (2, 'Kieran'), (3, 'Benjamin'), (5, 'Thomas'), (6, 'Gabriel'), (7, 'Bukayo')]
