print("Dog, Cat, Mouse, Elephants".split())
# by default split separates by empty spaces
# there will be: ['Dog,', 'Cat,', 'Mouse,', 'Elephants']

print("Dog, Cat, Mouse, Elephants".split(","))
# but now we have spaces which we did not want to have as well
# ['Dog', ' Cat', ' Mouse', ' Elephants']

print("Dog, Cat, Mouse, Elephants".split(", "))
# the expected result finally:
# ['Dog', 'Cat', 'Mouse', 'Elephants']

