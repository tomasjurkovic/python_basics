# it allows me to create copy of list with its own reference
import copy

ex_1 = [1, 2, 3, 4, 5]
ex_2 = copy.deepcopy(ex_1)

# lets see
print(ex_1)
print(ex_2)

# then modify it
ex_2[2] = 5000

print(ex_1)  # prints [1, 2, 3, 4, 5] because we created new reference with function deepcopy
print(ex_2)  # prints [1, 2, 5000, 4, 5]

# here is another variable
ex_3 = ex_2
ex_3[4] = 100
# but when I modify it ex_3 (without ha, I change also ex_2
print(ex_3)  # prints [1, 2, 5000, 4, 100]
print(ex_2)  # prints [1, 2, 5000, 4, 100] as well because I did not use deepcopy function
