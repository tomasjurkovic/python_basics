def rectangular_prism(width, length, height):
    return width * length * height


user_width = int(input("Insert width: \n"))
user_length = int(input("Insert length: \n"))
user_height = int(input("Insert height: \n"))

print("Rectangle prism is: " + str(rectangular_prism(user_width, user_length, user_height)))

