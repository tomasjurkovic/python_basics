ex_4 = {"make": "Honda",
        "model": "Civic",
        "year": 2016}

# it is possible to assign it to the variable while using pop (but no need)
popped = ex_4.pop("model")
print(ex_4)  # prints {'make': 'Honda', 'year': 2016}
print(popped)  # prints Civic

# popping_not_existing_key = ex_4.pop("owner")
# it has KeyError: 'owner', because owner does not exist

# popitem removes the last key value in the dictionary without the argument:
ex_4.popitem()  # removes "model": "Civic"

print(ex_4)  # prints {'make': 'Honda'}
