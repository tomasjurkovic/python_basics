player_numbers = {1: "Aaron", 2: "Kieran", 3: "Benjamin", 5: "Thomas", 6: "Gabriel", 7: "Bukayo"}

print(player_numbers)
# prints {1: 'Aaron', 2: 'Kieran', 3: 'Benjamin', 5: 'Thomas', 6: 'Gabriel', 7: 'Bukayo'}

more_player_numbers = player_numbers
more_player_numbers[8] = "Martin"
print(more_player_numbers)
# prints {1: 'Aaron', 2: 'Kieran', 3: 'Benjamin', 5: 'Thomas', 6: 'Gabriel', 7: 'Bukayo', 8: 'Martin'}
print(player_numbers)
# also prints {1: 'Aaron', 2: 'Kieran', 3: 'Benjamin', 5: 'Thomas', 6: 'Gabriel', 7: 'Bukayo', 8: 'Martin'}
# because we updated also the original dictionary, the new one is just a reference
