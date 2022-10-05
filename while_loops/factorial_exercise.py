user_number = int(input("Insert som number and program will print a factorial of inserted number: "))

interval = range(1, user_number + 1)
result = 1

for number in interval:
    result *= number
    number += 1

# this prints factorial number of the inserted number
print(result)
