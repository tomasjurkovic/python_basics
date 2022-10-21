# add method example
scifi = {"Matrix", "Star Wars", "Star Trek"}
print(scifi)  # prints {'Matrix', 'Star Trek', 'Star Wars'} in random order
scifi.add("Duna")
print(scifi)  # prints {'Matrix', 'Star Trek', 'Duna', 'Star Wars'} in random order

# remove method example
fruits = {"apple", "banana", "grapefruit", "tomato"}
print(fruits)  # prints {'grapefruit', 'banana', 'apple', 'tomato'} in random order
fruits.remove("tomato")
print(fruits)  # prints {'grapefruit', 'banana', 'apple'} in random order

# fruits.remove("pear") in this case KeyError: 'pear' error would be displayed
# because pear is not available in our fruits set
# in this case we could better use discard method and we won't get any error if it is not there

# discard method example
fruits.discard("pear")  # no error in console
fruits.discard("banana")  # banana is removed from fruits set
print(fruits)  # prints {'apple', 'grapefruit'} in random order

# clear method example:
scifi.clear()  # it takes no argument
print(scifi)  # all cleared so only set() is printed
