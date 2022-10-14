ex_1 = [1, 2, 3]
ex_1[1] = 5
print(ex_1)  # prints [1, 5, 3]

ex_2 = "123"
# ex_2[1] = 6
# print(ex_2)  # 'str' object does not support item assignment
ex_2 = "153"
print(ex_2)  # we can just change whole string

# we should reassign values to the strings
ex_3 = "No, you can't"
ex_4 = "Yes" + ex_3[2:11] + "!"
print(ex_4)  # Yes, you can! is printed

ex_5 = [1, 2, 3, 4, 5]  # new list
ex_6 = ex_5  # another list that equals the previous one
ex_6[2] = 49  # I change third number of list ex_6, but I changed list ex_5 with this action as well
print(ex_6)  # prints [1, 2, 49, 4, 5] 
print(ex_5)  # prints [1, 2, 49, 4, 5] as well, because it is just a reference

