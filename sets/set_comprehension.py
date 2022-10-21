comp_1 = {even+2 for even in range(2, 11, 2)}
print(comp_1)
# prints {4, 6, 8, 10, 12}, because normally it would print even from 2 to 10, but we added +2

comp_2 = {char.lower() for char in "ALLCAPS"}
print(comp_2)
# prints {'c', 'l', 'a', 'p', 's'} in random order. We used lower() method, so characters are in lowercase
# repeated c and l are printed just once