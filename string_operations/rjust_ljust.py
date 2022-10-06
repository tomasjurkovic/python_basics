print("Hello World".rjust(15))
# it adds 4 empty spaces from the right, because string has 11 characters already
# together there are 15 characters

print("Hello World".ljust(15) + "it adds 4 characters to the left and this text comes after that.")

# it accepts second argument as well:
print("I put 3 stars after text".ljust(27, '*'))
print("I put 4 dots before text".rjust(28, '.'))
