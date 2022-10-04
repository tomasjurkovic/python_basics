# it is now an integer:
# if user inserts string, float or boolean, it returns error:
user_int = int(input("Please enter an integer: "))

print(user_int)
print(type(user_int))

# it is now an float:
# if user inserts string or boolean, it returns error:
# if user insert integer, it is converted to float - 10 = 10.0
user_float = float(input("Please enter an float value: "))

print(user_float)
print(type(user_float))