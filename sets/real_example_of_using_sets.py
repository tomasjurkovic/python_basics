# in this list there are multiple cities inserted multiple times:
olympic_cities = ["Athens", "Paris", "St. Louis", "Athens", "London", "Stockholm", "Berlin", "Antwerp",
                  "Paris", "Amsterdam", "Los Angeles", "Berlin", "Tokyo", "London", "London", "Helsinki",
                  "Melbourne", "Rome", "Tokyo", "Mexico City", "Munich", "Montreal", "Moscow", "Los Angeles",
                  "Seoul", "Barcelona", "Atlanta", "Sydney", "Athens", "Beijing", "London", "Rio", "Tokyo",
                  "Paris", "Los Angeles", "Brisbane"]

print(set(olympic_cities))
print(list(set(olympic_cities)))
# both prints:
# ['St. Louis', 'Seoul', 'Sydney', 'Tokyo', 'Montreal', 'Moscow', 'Beijing', 'London', 'Athens', 'Rio', 'Berlin',
# 'Los Angeles', 'Antwerp', 'Paris', 'Barcelona', 'Amsterdam', 'Munich', 'Helsinki', 'Rome', 'Mexico City',
# 'Melbourne', 'Brisbane', 'Atlanta', 'Stockholm']
# each city is printed just once
print(len(olympic_cities))  # prints 36
print(len((list(set(olympic_cities)))))  # prints 24
