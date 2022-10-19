city_info = {"country": "Canada", "province": "Ontario", "city": "Toronto"}
population = {"population": 2930000}
city_info.update(population)
# it updates city_info, but value in population stays same

print(city_info)
# prints {'country': 'Canada', 'province': 'Ontario', 'city': 'Toronto', 'population': 2930000}

print(population)
# prints {"population": 2930000}

# when we update the value of population:
city_info["population"] = 3000000

print(city_info)
# prints {'country': 'Canada', 'province': 'Ontario', 'city': 'Toronto', 'population': 3000000}
# we updated it only in city_info dictionary
print(population)
# value in population stays same
# prints {"population": 2930000}
