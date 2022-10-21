mountains = {"Mount Blanc", "Etna", "Kilimanjaro", "Mount Everest"}
hills = mountains.copy()
print(hills)  # prints {'Etna', 'Kilimanjaro', 'Mount Everest', 'Mount Blanc'} in random order
print(mountains)  # prints {'Etna', 'Kilimanjaro', 'Mount Everest', 'Mount Blanc'} in random order

print(hills is mountains)  # print False
# why? Because they are not the same sets

hills.add("Gerlachovsky peak")
print(hills)  # prints {'Mount Blanc', 'Kilimanjaro', 'Gerlachovsky peak', 'Mount Everest', 'Etna'} in random order
print(mountains)  # prints {'Mount Blanc', 'Kilimanjaro', 'Mount Everest', 'Etna'} in random order

# original set mountains was not edited, because there are two sets that are independent
