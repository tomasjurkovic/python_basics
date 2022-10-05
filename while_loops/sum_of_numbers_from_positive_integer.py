positive_number = int(input("Insert positive number: \n"))
the_sum = 0
growing_number = 1

while growing_number <= positive_number:
    the_sum = the_sum + growing_number
    growing_number += 1


print("The inserted number was: " + str(positive_number) + ".")
print("The result is: " + str(the_sum) + ".")


# reversed logic:
positive_number_2 = int(input("Insert another positive number: \n"))
the_sum_2 = 0
decreasing_number = positive_number_2

while decreasing_number >= 1:
    the_sum_2 = the_sum_2 + decreasing_number
    decreasing_number -= 1


print("The inserted number was: " + str(positive_number_2) + ".")
print("The result is: " + str(the_sum_2) + ".")