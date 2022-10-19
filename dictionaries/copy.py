player_numbers = {1: "Aaron", 2: "Kieran", 3: "Benjamin", 5: "Thomas", 6: "Gabriel", 7: "Bukayo"}

print(player_numbers)
# prints {1: 'Aaron', 2: 'Kieran', 3: 'Benjamin', 5: 'Thomas', 6: 'Gabriel', 7: 'Bukayo'}

more_player_numbers = player_numbers.copy()
more_player_numbers[8] = "Martin"
# with copy it does not affect previous dictionary

print(more_player_numbers)
# prints {1: 'Aaron', 2: 'Kieran', 3: 'Benjamin', 5: 'Thomas', 6: 'Gabriel', 7: 'Bukayo', 8: 'Martin'}
print(player_numbers)
# prints {1: 'Aaron', 2: 'Kieran', 3: 'Benjamin', 5: 'Thomas', 6: 'Gabriel', 7: 'Bukayo'}
