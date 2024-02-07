# Write Python code to print the seventh number of range(0, 25, 3).

# seventh_number = list(range(0, 25, 3))
# print(seventh_number[6])

# my_range = range(0, 25, 3)[6]
# print(my_range)

# Use slicing to write Python code to print a 6-character substring of 'Launch School' that begins with the first c.

# my_str = 'Launch School'

# # solution 1
# print(my_str[4:10])

# # solution 2
# start = my_str.find('c')
# print(my_str[start:start + 6])

# Write Python code to create a new tuple from (1, 2, 3, 4, 5). The new tuple should be in reverse order from the original. It should also exclude the first and last members of the original. The result should be the tuple (4, 3, 2)

# my_tuple = (1, 2, 3, 4, 5)

# # solution 1 using slice
# my_second_tuple = my_tuple[1:len(my_tuple) - 1]
# reversed_tuple = my_second_tuple[::-1]
# print(reversed_tuple)

# # solution 2 using list constructor
# my_second_tuple = my_tuple[1:len(my_tuple) - 1]
# my_list = list(my_second_tuple)
# my_list.reverse()
# result = tuple(my_list)
# print(result)

# pets = {
#     'Cat':  'Meow',
#     'Dog':  'Bark',
#     'Bird': 'Tweet',
# }

# Part 1: Write some code to print Bark by accessing the Dog element.
# print(pets['Dog'])

# Part 2: Write some code to print None when you try to print the value associated with the non-existent key, `Lizard'.
# pets['Lizard'] = 'None'
# print(pets['Lizard'])
# print(pets.get('Lizard'))

# Part 3: Write some code to print <silence> when you try to print the value associated with the non-existent key, `Lizard'.
# pets['Lizard'] = '<silence>'
# print(pets['Lizard'])
# print(pets.get('Lizard', '<silence>'))

# Which of the following values can't be used as a key in a dict, and why?
# keys must be hashable, or immutable
# 'cat' 
# (3, 1, 4, 1, 5, 9, 2)
# ['a', 'b'] # no
# {'a': 1, 'b': 2} # no
# range(5)
# {1, 4, 9, 16, 25} # no
# 3
# 0.0
# frozenset({1, 4, 9, 16, 25})

# What will the following code print?

# print('abc-def'.isalpha()) # F
# print('abc_def'.isalpha()) # T / F
# print('abc def'.isalpha()) # F
# print('abc def'.isalpha() and 
#       'abc def'.isspace()) # F
# print('abc def'.isalpha() or 
#       'abc def'.isspace()) # F
# print('abcdef'.isalpha()) # T
# print('31415'.isdigit()) # T
# print('-31415'.isdigit()) # T / F
# print('31_415'.isdigit()) # F
# print('3.1415'.isdigit()) # T / F
# print(''.isspace()) # F

# Write Python code to replace all the : characters in the string below with +.

# info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'

# split_info = info.split(':')
# print(split_info)

# result = '+'.join(split_info)
# print(result)

# result = info.replace(':', '+')
# print(result)

# Explain why the code below prints different values on lines 3 and 4.

# text = "It's probably pining for the fjords!"

# print(text[21:35].rfind('f'))     # 8
# print(text.rfind('f', 21, 35))    # 29
# print(len(text)) # 36
# 'or the fjords!'
# creates a new string so the slice indexes `o` at 0'

# Write some code to replace the value 6 in the following nested list with 606:

# stuff = [
#     ['hello', 'world'],
#     ['example', 'mem', None, 6, 88],
#     [4, 8, 12]
# ]

# stuff[1][3] = 606
# print(stuff)

# cats = {
#     'Pete': {
#         'Cheddar': {
#             'color': 'orange',
#             'enjoys': {
#                 'sleeping',
#                 'snuggling',
#                 'meowing',
#                 'eating',
#                 'birdwatching',
#             }
#         },
#         'Cocoa': {
#             'color': 'black',
#             'enjoys': {
#                 'eating',
#                 'sleeping',
#                 'playing',
#                 'chewing',
#             }
#         },
#     }
# }
# # $600 deductible, then 80% benefits
# print(cats['Pete']['Cocoa']['enjoys'])

# Without running the following code, determine what each line should print.

# print('johnson' in 'Joe Johnson') # F
# print('sen' not in 'Joe Johnson') # T
# print('Joe J' in 'Joe Johnson') # T
# print(5 in range(5)) # F
# print(5 in range(6)) # T
# print(5 not in range(5, 10)) # F
# print(0 in range(10, 0, -1)) # F
# print(4  in {6, 5, 4, 3, 2, 1}) # T
# print({1, 2, 3} in {1, 2, 3}) # T / F
# print({3, 2} in {1, frozenset({2, 3})}) # T

# Write some code that determines and prints whether the number 3 appears inside each of these lists:

# numbers1 = [1, 3, 5, 7, 9, 11]
# numbers2 = []
# numbers3 = [2, 4, 6, 8]
# numbers4 = ['1', '3', '5']
# numbers5 = ['1', 3.0, '5']

# print(3 in numbers1)
# print(3 in numbers2)
# print(3 in numbers3)
# print(3 in numbers4)
# print(3 in numbers5)

# Without running the following code, determine what each print statement should print.

# cats = ('Cocoa', 'Cheddar',
#         'Pudding', 'Butterscotch')
# print('Butterscotch' in cats) # T
# print('Butter' in cats) # T / F
# print('Butter' in cats[3]) # T
# print('cheddar' in cats) # F

# Assume you have the following sequences:

# my_str = 'abc'
# my_list = ['Alpha', 'Bravo', 'Charlie']
# my_tuple = (None, True, False)
# my_range = range(10, 60, 10)

# Write some code that combines the sequences into a list of tuples. Each tuple should contain one member of each sequence. Print the final result so you can see all the values, which should look like this:

# zipped_iterables = zip(my_str, my_list, my_tuple, my_range)
# print(list(zipped_iterables))

# Without running the following code, what values will be printed by line 10?

# pets = {
#     'Cat':  'Meow',
#     'Dog':  'Bark',
#     'Bird': 'Tweet',
# }

# keys = pets.keys() # [['Cat'], ['Dog'], ['Bird]]
# del pets['Dog'] # {'Cat': 'Meow','Bird': 'Tweet'}
# pets['Snake'] = 'Sssss' # {'Cat': 'Meow','Bird': 'Tweet', 'Snake': 'Sssss'}
# print(keys) # [['Cat'], ['Snake'], ['Bird]]