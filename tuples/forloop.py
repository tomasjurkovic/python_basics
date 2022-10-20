# for loop example:

major_cities = ("Tokyo", "London", "New York", "Shanghai", "Sydney")

for city in major_cities:
    print(city)

# while example:
big_cities = ("Tokyo", "London", "New York", "Shanghai", "Sydney")

count = 0
while count < len(big_cities):
    print(major_cities[count])
    count += 1

# both prints same:
# Tokyo
# London
# New York
# Shanghai
# Sydney

# backward:
count_2 = len(big_cities) - 1
print(count_2)
while count_2 >= 0:
    print(big_cities[count_2])
    count_2 -= 1

# prints:
# Sydney
# Shanghai
# New York
# London
# Tokyo