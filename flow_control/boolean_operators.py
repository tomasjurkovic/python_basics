# AND STATEMENT:
# True and True example:
print(4 > 1 and "world" == "world") # prints True
# True and False example:
print(17.8 >= 17.80 and 2 != 2) # prints False
# False and True example:
print("earth" == "Earth" and 6 <= 6) # prints False
# False and False example:
print("earth" == "Earth" and 6 != 6) # prints False

# OR STATEMENT:
# True and True example:
print(4 > 1 or "world" == "world") # prints True
# True and False example:
print(17.8 >= 17.80 or 2 != 2) # prints True
# False and True example:
print("earth" == "Earth" or 6 <= 6) # prints True
# False and False example:
print("earth" == "Earth" or 6 != 6) # prints False

# NOT STATEMENT:
# it just prints opposite of statements:
print(not 1000 > 1) # prints False - because without 'not' it's True
print(not "Python" != "Python") # prints True - because without 'not' it's False
