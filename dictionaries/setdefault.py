computers = {"Google": "Chromebook", "Apple": "MacBook", "Microsoft": "Surface Pro"}

if "Lenovo" not in computers:
    computers["Lenovo"] = "ThinkPad"

print(computers)
# prints {'Google': 'Chromebook', 'Apple': 'MacBook', 'Microsoft': 'Surface Pro', 'Lenovo': 'ThinkPad'}

computers.setdefault("Dell", "Latitude")
# this makes the same as code above

print(computers)
# prints:
# {'Google': 'Chromebook', 'Apple': 'MacBook', 'Microsoft': 'Surface Pro', 'Lenovo': 'ThinkPad', 'Dell': 'Latitude'}

# but when the key value pair already was added, then its value is not rewritten
computers.setdefault("Dell", "Another model")
# it's same if I call this method on key value pair that already exists in dictionary
computers.setdefault("Google", "Google book")

print(computers)
# prints:
# {'Google': 'Chromebook', 'Apple': 'MacBook', 'Microsoft': 'Surface Pro', 'Lenovo': 'ThinkPad', 'Dell': 'Latitude'}
