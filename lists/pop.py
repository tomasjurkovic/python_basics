bands = ["Queen", "Mr. Big", "Nirvana", "Guns 'N Roses", "Kiss", "Alice In Chains"]
end = bands.pop()  # it assigns to the variable end last band in the list => Alice In Chains
# and removes this band from the list 'bands'
print(bands)  # prints ["Queen", "Mr. Big", "Nirvana", "Guns 'N Roses", "Kiss"]
print(end)  # prints Alice In Chains

axl_and_slash = bands.pop(3)  # we can take item from the list based on its index number
# it removes selected band from the list 'bands' as well
print(axl_and_slash)  # prints Guns 'N Roses
print(bands)  # prints ["Queen", "Mr. Big", "Nirvana", "Kiss"]
