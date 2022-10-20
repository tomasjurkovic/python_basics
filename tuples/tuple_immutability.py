tuple_8 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# tuple_8[0] = 100
# this would return error message: TypeError: 'tuple' object does not support item assignment

# it is useful for example for:
weeks = ("Monday",
         "Tuesday",
         "Wednesday",
         "Thursday",
         "Friday",
         "Saturday",
         "Sunday")

seasons = ("Fall",
           "Winter",
           "Spring",
           "Summer")

# tuples takes less space in memory, lets compare it with list
list_8 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(tuple_8.__sizeof__())  # prints 104
print(list_8.__sizeof__())  # prints 120 which is more than 104

# also it is useful like this inside the dictionary:
occupations = {("Angus", "Young"): "musican",
               ("Narendra", "Modi"): "prime minister",
               ("Richard", "Branson"): "enterpreneur",
               ("Quentin", "Tarantino"): "movie director"}
