from random import *

nmr_of_gallons_of_gas = randint(10, 25)
nmr_of_miles_with_full_tank = randint(200, 400)

# I used floor division instead of division:
print("The car can travel " + str(nmr_of_miles_with_full_tank // nmr_of_gallons_of_gas) + " with one gallon of gas.")
print("The car's fuel tank can hold " + str(nmr_of_gallons_of_gas) + " gallons.")
print("The car can travel " + str(nmr_of_miles_with_full_tank) + " miles on a full tank")
