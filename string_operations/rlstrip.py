# when I want to remove characters from the string
# by default it is empty characters
# but it can be any character or multiple characters
# arguments need to be strings

print(" remove those empty spaces from both sides   ".strip())
# prints: "remove those empty spaces from both sides"

print(" remove those empty spaces from right side   ".rstrip())
# prints: " remove those empty spaces from right side"

print(" remove those empty spaces from left side   ".lstrip())
# prints: "remove those empty spaces from right side   "

print("I had an exciting trip!!!1111".rstrip("!1"))
# it removes "!" and "1" characters from the right side of that string
print("I had an exciting trip!!!1111".lstrip("!1"))
# removes nothing, because first character is 'I'

print("blueuueuueblueueueyellowbluuueblue".strip("lebu"))
# yellow - stays in this example, becuase it removes each 'b', 'l', 'u' and 'e' characters
# until it finds another from each side
