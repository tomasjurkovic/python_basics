user_num = int(input("Please enter the integer: \n"))

# elif statements run only when if statement was 'False' and each elif statement before was 'False' as well
if user_num < 0:
    print("The number you entered is less than 0.")
elif user_num == 0:
    print("The number you entered is 0.")
elif 0 < user_num <= 100:
    print("The number you entered is between 1 and 100.")
else:
    print("The number you entered is higher than 100.")
