# In your own words, explain the difference between these two expressions.

# my_object1 == my_object2 # the two objects store the same values but are separate objects in memory
# my_object1 is my_object2 # the two objects are the exact same object in memory

# Without running this code, what will it print? Why?

# set1 = {42, 'Monty Python', ('a', 'b', 'c')}
# set2 = set1
# set1.add(range(5, 10))
# print(set2)

# {42, 'Monty Python', ('a', 'b', 'c'), 5, 6, 7, 8, 9}
# {42, 'Monty Python', ('a', 'b', 'c'), range(5, 10)}

# Without running this code, what will it print? Why?

# dict1 = {
#     "Hitchhiker's Guide to the Galaxy": 42,
#     'Monty Python': 'The Life of Brian',
#     'Airplane!': "Don't call me Shirley!",
# }

# dict2 = dict(dict1)
# dict2['Monty Python'] = 'Holy Grail'
# print(dict1['Monty Python'])

# 'The Life of Brian'
# `dict2` created a shallow copy of `dict1`. `dict1` reassigns one of it key value pairs to an entirely new object, so `dict2` no longer references the corresponding object value of `Monty Python`.

# Without running this code, what will it print? Why?

# dict1 = {
#     'a': [1, 2, 3],
#     'b': (4, 5, 6),
# }

# dict2 = dict(dict1)
# dict1['a'][1] = 42
# print(dict2['a'])

# dict2 is assigned to a shallow copy of dict1
# dict1 mutates the referenced list corresponding to the `a` key. The element 2 in the nested reference list is also reassigned to 42. 
# dict2 also references the same pointer to this mutated list
# the code prints [1, 42, 3]
# this code demonstrates that when two objects are shallow copies of each other, mutating a shared reference in one object will reflect in the other object. 

# Write some code to create a deep copy of the dict1 object and assign it to dict2. You should only modify the code where indicated.

# import copy

# dict1 = {
#     'a': [[7, 1], ['aa', 'aaa']],
#     'b': ([3, 2], ['bb', 'bbb']),
# }

# dict2 = copy.deepcopy(dict1)

# All of these should print False
# print(dict1         is dict2)
# print(dict1['a']    is dict2['a'])
# print(dict1['a'][0] is dict2['a'][0])
# print(dict1['a'][1] is dict2['a'][1])
# print(dict1['b']    is dict2['b'])
# print(dict1['b'][0] is dict2['b'][0])
# print(dict1['b'][1] is dict2['b'][1])

# All of these should print True

# print(dict1['a'][0][0] is dict2['a'][0][0])
# print(dict1['a'][0][1] is dict2['a'][0][1])
# print(dict1['a'][1][0] is dict2['a'][1][0])
# print(dict1['a'][1][1] is dict2['a'][1][1])
# print(dict1['b'][0][0] is dict2['b'][0][0])
# print(dict1['b'][0][1] is dict2['b'][0][1])
# print(dict1['b'][1][0] is dict2['b'][1][0])
# print(dict1['b'][1][1] is dict2['b'][1][1])

# The following program is nearly identical to that of the previous exercise. However, this time, it should create a shallow copy of dict1. Be careful: you're not allowed to use the copy module in this exercise.`

# In addition, before you run this code, can you predict the output values?

dict1 = {
    'a': [{7, 1}, ['aa', 'aaa']],
    'b': ({3, 2}, ['bb', 'bbb']),
}

dict2 = dict(dict1)

print(dict1         is dict2) # False
print(dict1['a']    is dict2['a']) # True
print(dict1['a'][0] is dict2['a'][0]) # True
print(dict1['a'][1] is dict2['a'][1]) # True
print(dict1['b']    is dict2['b']) # True
print(dict1['b'][0] is dict2['b'][0]) # True
print(dict1['b'][1] is dict2['b'][1]) # True