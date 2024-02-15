# Create a dictionary that contains the following data, and assign it to a variable named car.

# car = {
#     'type': 'sedan', 
#     'color': 'blue', 
#     'mileage': 80_000, 
# }
# print(car)

# Add some code below the following code to define a year key with a value of 2003. Don't update the dictionary literal; instead, add some code after lines 1-5:

# car = {
#     'type':    'sedan',
#     'color':   'blue',
#     'mileage': 80_000,
# }

# car['year'] = 2003

# Using the following code, delete the 'mileage' key and its associated value from car.

# car = {
#     'type':    'sedan',
#     'color':   'blue',
#     'mileage': 80_000,
#     'year':    2003,
# }

# del car['mileage']
# print(car)

# Using the following code, select and print the value 'blue' from the car object:

# car = {
#     'type':  'sedan',
#     'color': 'blue',
#     'year':  2003,
# }

# print(car['color'])

# Calculate and print the number of key/value pairs in the following dictionary:

# car = {
#     'type':  'sedan',
#     'color': 'blue',
#     'year':  2003,
# }

# print(len(car))

# Check whether the keys 'name' and 'grade' exist in the following dictionary:

# student = {
#     'id': 123,
#     'grade': 'B',
# }

# print(student.get('grade'))
# print(student.get('name', 0))

# Create a nested dictionary that contains the following data.

# multiple_cars = {
#     'Car': {
#         'type': 'sedan',
#         'color': 'blue',
#         'year': 2003,
#     },
#     'Truck': {
#         'type': 'pickup',
#         'color': 'red',
#         'year': 1998,
#     },
# }

# print(multiple_cars)

# Rewrite car as a nested list containing the same key/value pairs.

# car = {
#     'type':  'sedan',
#     'color': 'blue',
#     'year':  2003,
# }

# car = [['type','sedan'], ['color': 'blue'], ['year':  2003]]

# Use a for loop to iterate over the numbers dictionary and return a list containing each number divided by 2. Assign the returned list to a variable named half_numbers and print its value using print.

# numbers = {
#     'high':   100,
#     'medium': 50,
#     'low':    10,
# }

# [50, 25, 5]

# using list comprehension

# half_numbers = [numbers[number] // 2 for number in numbers]
# print(half_numbers)

# half_numbers = []
# values = numbers.values()

# for value in values:
#     half_numbers.append(value // 2)
# print(half_numbers)

# Use a for loop to iterate over the numbers dictionary and print each element's key/value pair.

numbers = {
    'high':   100,
    'medium': 50,
    'low':    10,
}

for number in numbers:
    print(f'A {number} number is {numbers[number]}.')
# A high number is 100.
# A medium number is 50.
# A low number is 10.