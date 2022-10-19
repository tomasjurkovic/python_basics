# this creates dictionary with 1 key and 1 value
ex_1 = {}.fromkeys(["address"], "Hlavna 1, Kosice")
print(ex_1)
# prints {'address': 'Hlavna 1, Kosice'}

# now each character is specific key, value is always same
ex_2 = {}.fromkeys("ad", "Hlavna 1, Kosice")
print(ex_2)
# prints {'a': 'Hlavna 1, Kosice', 'd': 'Hlavna 1, Kosice'}

# when only one argument, then default value is None
ex_3 = {}.fromkeys(["address"])
print(ex_3)
# prints {'address': None}
