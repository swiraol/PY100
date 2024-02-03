# Concatenate two strings, one with your first name and one with your last, to create a new string with your full name as its value. For example, if your name is John Doe, you should combine 'John' and 'Doe' to get 'John Doe'.

# print('Robert' + ' ' + 'Tsui')
# print(f'Robert Tsui')
# first_name = 'Robert'
# last_name = 'Tsui' 
# print(f'{first_name} {last_name}')

# Use the REPL and the arithmetic operators to extract the individual digits of 4936:
# nums = 4936
# # One place is 6.
# nums % 10 # 6

# # Tens place is 3.
# nums = nums // 10 # 493
# num % 10 # 3

# # Hundreds place is 9.
# nums = nums // 10 # 49
# nums % 10 # 9

# # Thousands place is 4.
# nums = nums // 10 # 4
# nums # 4

# What does the following code do? Why?

# print('5' + '10')

# Refactor the code from the previous exercise to use coercion to print 15 instead.

# print(type(int('5') + int('10')).__name__)

# Will an error occur if you try to access a list element with an index greater than or equal to the list's length? For example:

# foo = ['a', 'b', 'c']
# print(foo[3])      # will this result in an error?

# yes, IndexError: list index out of range

# To what value does the following expression evaluate?

# 'foo' == 'Foo'

# False

# What will the following code do? Why?

# int('3.1415')

# it coerces the string into an integer `3`. 

# that's not right, the interpreter needs to recognize it as a float first. 

# number = float('3.1415')

# there. now we can invoke the int function and pass in a float number to convert it into an integer.
# number = int(number)

# should return 3

# print(number)

# To what value does the following expression evaluate?

# '12' < '9'

# True because '1' is less than '9' according to their corresponding ASCII character codes
