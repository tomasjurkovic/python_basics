interval = range(1, 51)
# range that goes from 1 to 50

for number in interval:
    divided_by_3 = number % 3
    divided_by_5 = number % 5

    # when number is divided by 3 & 5 prints 'Fizz Buzz'
    if divided_by_5 == 0 and divided_by_3 == 0:
        print("Fizz Buzz")

    # when number is divided by 3 but not by 5 prints just 'Fizz'
    elif divided_by_3 == 0 and divided_by_5 != 0:
        print("Fizz ")

    # when number is divided by 5 but not by 3 prints just 'Buzz'
    elif divided_by_5 == 0 and divided_by_3 != 0:
        print("Buzz")

    # when number is not divided by 5 and 3 prints just 'number itself'
    else:
        print(number)
