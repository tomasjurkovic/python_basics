print("Mixed LetterS".isupper())
# it prints False, because there are upper and lower letters as well

print("IS UPPER?".isupper())
# it prints True

print("is lower?".islower())
# it prints True

print("I am Not sure".islower())
# it prints False, because there are upper and lower letters as well

print("!@#$%^&^%$#@#$%^&".islower())
# it has to contain at least one letter.
# Now it contains only special characters, so result is False even for isupper() function

print("".islower())
# it is same for empty string
