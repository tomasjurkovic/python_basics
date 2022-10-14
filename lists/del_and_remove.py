# this is how we can use del method to delete item in the list

planets = ["Pluto", "Mars", "Earth", "Venus"]
del planets[0]  # removes Pluto, because it's not planet anymore and we deleted it with this method
print(planets)  # prints ['Mars', 'Earth', 'Venus']

# del removes items based on the index number

planets_2 = ["Pluto", "Mars", "Earth", "Venus"]
planets_2.remove("Pluto")  # removes Pluto, because it's not planet anymore and we deleted it with this method
print(planets_2)  # prints ['Mars', 'Earth', 'Venus']

colors = ["blue", "red", "orange", "white", "blue", "purple", "blue", "yellow"]
colors.remove("blue")  # only the first item 'blue' is removed, not all in the list
print(colors)  # prints ["red", "orange", "white", "blue", "purple", "blue", "yellow"]

# remove method removes item when it finds that item
