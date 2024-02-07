# If you have a list named people, how can you determine the number of entries in that list?

# use the len function

# Can you write some code to change the value 'bye' in the following tuple to 'goodbye'?

# stuff = ('hello', 'world', 'bye', 'now')
# stuff = list(stuff)
# stuff[2] = 'goodbye'
# stuff = tuple(stuff)
# print(stuff)

# Identify at least 2 differences between lists and tuples. Identify at least 2 ways that lists and tuples are similar.

# differences
    # tuples are immutable, lists are mutable
    # list literals use [], tuple literals use ()
# similarities    
    # tuples and lists are heterogenous
    # they both contain ordered sequences and their members can be accessed with numeric indexes

# Why can we treat strings as sequences?

# string characters are ordered and can be accessed with numeric indexes 

# How do the set types differ from the sequence types?

# set types are unordered and its key value pairs cant be indexed

# pi = 3.141592

# Write some code that converts the value of pi to a string and assigns it to a variable named str_pi.

# str_pi = str(pi)
# print(str_pi)

# Without running the following code, identify the numbers that are included in each of the following ranges:

# range(7) # [0 through 6]
# range(1, 6) # [1 through 5]
# range(3, 15, 4) # [3, 7, 11]
# range(3, 8, -1) # []
# range(8, 3, -1) # [8, 7, 6, 5, 4]

# How would you print all the numbers in the following range?

# range(3, 17, 4)
# list = list(range(3, 17, 4))
# print(list)

# my_list = [1, 2, 3, [4, 5, 6]]
# another_list = list(my_list)

# Are the lists assigned to my_list and another_list equal?
# yes they contain the same elements

# Are the lists assigned to my_list and another_list the same object?
# No, the `list` constructor creates a new object

# Are the nested lists at index 3 of my_list and another_lists equal?
# yes, they are equal they have the same elements

# Are the nested lists at index 3 of my_list and another_lists the same object?
# yes, `another_list` is a shallow copy of `my_list` and both contain the same reference to the nested list

# Bob expects the following code to print the names in alphabetical order. Without running the code, can you say whether it will? Explain your answer.

# names = { 'Chris', 'Karis', 'Max', 'Nick',
#           'Karl', 'Clare', 'Victor' }
# print(names)

# No, sets are unordered sequences but will not be sorted alphabetically

# data = {
#     'Alice': 'USA', 
#     'Francois': 'Canada', 
#     'Inti': 'Peru', 
#     'Monika': 'Germany', 
#     'Sanyu': 'Uganda', 
#     'Yoshitaka': 'Japan'
# }

# print(data['Alice'])
