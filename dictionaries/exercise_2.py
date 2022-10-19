# create a variable and assign it the following dictionary:
# make the dictionary span multiple lines so that the line the dictionary starts on is not too long.
famous_songs = {"Queen": "Bohemian Rhapsody",
                "Bee Gees": "Stayin' Alive",
                "U2": "One",
                "Michael Jackson": "Billie Jean",
                "The Beatles": "Hey Jude",
                "Bob Dylan": "Like A Rolling Stone"}

# print the length of the dictionary.
print(len(famous_songs))  # 6 is printed

# use the .keys() method and a for loop to get and print all of the keys from the dictionary on separate lines.
for key in famous_songs.keys():
    print(key)

# prints: Queen
# Bee Gees
# U2
# Michael Jackson
# The Beatles
# Bob Dylan

# print all of the values from the dictionary using the .values() method.
for value in famous_songs.values():
    print(value)

# prints: Bohemian Rhapsody
# Stayin' Alive
# One
# Billie Jean
# Hey Jude
# Like A Rolling Stone

# use .items() with a for loop to iterate through and print all of the key value pairs from the dictionary.
for key, value in famous_songs.items():
    print(key, value)

# prints: Queen Bohemian Rhapsody
# Bee Gees Stayin' Alive
# U2 One
# Michael Jackson Billie Jean
# The Beatles Hey Jude
# Bob Dylan Like A Rolling Stone
# This song was not found among the famous songs

# use the .get() method to check the dictionary for the key
# and create a message that will print if the key is not found in the dictionary.
print(famous_songs.get("Promise of the Real", "This song was not found among the famous songs"))
