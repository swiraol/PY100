# Write a function that returns the first element of a list provided as an argument. For example:

# def first(list):
#     if list:
#         return list[0]
#     else:
#         return None

# print(first(['Earth', 'Moon', 'Mars']))  # Earth
# print(first([]))

# Write a function that returns the last element of a list provided as an argument. For example:

# def last(lst):
#     return None if not lst else lst[len(lst) - 1]
# print(last(['Earth', 'Moon', 'Mars']))  # Mars
# print(last([]))

# We are given the following list of energy sources.

# energy = ['fossil', 'solar', 'wind', 'tidal', 'fusion']

# Write some code to remove 'fossil' from the list, then add 'geothermal' to the end of the list.

# def energy_sources(lst):
#     lst.pop(0)
#     lst.append('geothermal')
#     return lst

# print(energy_sources(energy))

# Split the string alphabet into a list of characters.

# alphabet = 'abcdefghijklmnopqrstuvwxyz'

# print(list(alphabet))

# Count the number of elements in scores that are 100 or above.

# scores = [96, 47, 113, 89, 100, 102]
# count = 0
# for number in scores:
#     if number >= 100:
#         count+= 1
# print(count)

# count = [score for score in scores if score >= 100]
# print(len(count))

# You've been given a list of vocabulary words grouped into sub-lists, by meaning. This is a two-dimensional list or a nested list. Write some code that iterates through and prints all the words, one per line.

# vocabulary = [
#     ['happy', 'cheerful', 'merry', 'glad'],
#     ['tired', 'sleepy', 'fatigued', 'drained'],
#     ['excited', 'eager', 'enthused', 'animated'],
# ]

# # happy
# # cheerful
# # merry
# # glad
# # tired
# # sleepy
# # etc...

# for list in vocabulary:
#     for word in list:
#         print(word)

# Predict the output of the code shown below. When you run the code, do you see what you expected? Why or why not?

# list1 = [2, 6, 4]
# list2 = [2, 6, 4]

# print(list1 == list2) # true because their values are compared, not their identities in memory

# How can you check if a variable holds a value that is a list? Given two variables, verify whether the values they hold are lists.

# some_value1 = [0, 1, 0, 0, 1]
# some_value2 = 'I leave you my Kingdom, take good care of it.'

# print(type(some_value1) == list)
# print(isinstance(some_value1, list))
# print(type(some_value2) == list)

# The destinations list contains a list of travel destinations.

# destinations = ['Prague', 'London', 'Sydney', 'Belfast',
#                 'Rome', 'Aruba', 'Paris', 'Bora Bora',
#                 'Barcelona', 'Rio de Janeiro', 'Marrakesh',
#                 'New York City']

# Write a function that, without using the built-in in operator, checks whether a specific destination is included within destinations. For example: When checking whether 'Barcelona' is contained in destinations, the expected output is True, whereas the expected output for 'Nashville' is False.

# def contains(city, cities):

#     for destination in cities:
#         if destination == city:
#             return True
#     return False 

# print(contains('Barcelona', destinations))  # True
# print(contains('Nashville', destinations))  # False

# We generated parts of a passcode and now want to combine them into a string. Write some code that returns a string, with each portion of the passcode separated by a hyphen (-).

# passcode = ['11', 'jZ5', 'hQ3f*', '8!7g3', 'p3Fs']

# Write some code here.
# Expected return value: '11-jZ5-hQ3f*-8!7g3-p3Fs'

# using join

# print('-'.join(passcode))

# using a while loop

# str = ''
# index = 0
# while index < len(passcode):
#     str += passcode[index]
#     if index == len(passcode) - 1:
#         pass  
#     else: 
#         str += '-'
#     index += 1
# print(str)

# using for loop and range function

# joined_passcode = ''

# for i in range(len(passcode)):
#     if i > 0:
#         joined_passcode += '-'
#     joined_passcode += passcode[i]
# print(joined_passcode)

# We have a grocery list. As we check off items on that list, we want to remove them from the list.

# Write code that removes the items from grocery_list, one by one, until it is empty. If you print the elements you remove, the expected behavior would look as follows.

grocery_list = ['paprika', 'tofu', 'garlic', 'quinoa',
                'carrots', 'broccoli', 'hummus']

for i in range(len(grocery_list)):
    print(i)
    print(grocery_list.pop(0))

print(grocery_list)

grocery_list = ['paprika', 'tofu', 'garlic', 'quinoa', 'carrots', 'broccoli', 'hummus']

# Iterate over a copy of the list using slice notation to create the copy
for item in grocery_list[:]:
    print(item)
    grocery_list.pop(0)
print(grocery_list)

# paprika
# tofu
# garlic
# quinoa
# carrots
# broccoli
# hummus
# []