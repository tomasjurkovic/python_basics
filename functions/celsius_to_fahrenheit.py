def convert_to_fahrenheit(celsius_value):
    fahrenheit = ((celsius_value * 18) + 32) / 10
    return float(fahrenheit)


user_celsius_value = int(input("Enter the valid Celsius value: \n"))

print("The Fahrenheit equivalent of " + str(user_celsius_value) + " degrees Celsius is "
      + str(convert_to_fahrenheit(user_celsius_value)) + ".")

