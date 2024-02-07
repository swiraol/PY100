# To what values do the following expressions evaluate?

# False or (True and False) # False
# True or (1 + 2) # True
# (1 + 2) or True # 3
# True and (1 + 2) # 3
# False and (1 + 2) # False
# (1 + 2) and True # True
# (32 * 4) >= 129 # False
# False != (not True) # False
# True == 4 # True / False
# False == (847 == '847') # True

# Write a function, even_or_odd, that determines whether its argument is an even or odd number. If it's even, the function should print 'even'; otherwise, it should print 'odd'. Assume the argument is always an integer.

# def even_or_odd(arg):
#     if arg % 2 == 0:
#         print('even')
#     else: print('odd')

# def even_or_odd(number):
#     print('even' if number % 2 == 0 else 'odd')

# result = even_or_odd(4)
# print(result)

# Without running the following code, what does it print? Why?

# def bar_code_scanner(serial):
#     match serial:
#         case '123':
#             print('Product1')
#         case '113':
#             print('Product2')
#         case '142':
#             print('Product3')
#         case _:
#             print('Product not found!')

# bar_code_scanner('113') # 'Product2' because serial == '113'
# bar_code_scanner(142) # `Product not found` because argument is an integer and an integer doesn't match any of the string

# Refactor this statement to use a regular if statement instead.

# return ('bar' if foo() else qux())

# if foo():
#     return 'bar'
# else:
#     return qux()

# What does this code output, and why?

# def is_list_empty(my_list):
#     if (my_list):
#         print('Not Empty')
#     else:
#         print('Empty')

# is_list_empty([])

# The code prints 'Empty' because `[]` is a falsy value so the else clause executes.

# Write a function that takes a string as an argument and returns an all-caps version of the string when the string is longer than 10 characters. Otherwise, it should return the original string. Example: change 'hello world' to 'HELLO WORLD', but don't change 'goodbye'.

# def caps_long(string):
#     if len(string) > 10:
#         return string.upper()
#     else: 
#         return string

# print(caps_long('hello world'))
# print(caps_long('goodbye'))
# print(caps_long("Sue Smith"))     # Sue Smith
# print(caps_long("Sue Roberts"))   # SUE ROBERTS
# print(caps_long("Joe Shea"))      # Joe Shea
# print(caps_long("Joe Stevens"))   # JOE STEVENS
    
# Write a function that takes a single integer argument and prints a message that describes whether:
# the value is between 0 and 50 (inclusive)
# the value is between 51 and 100 (inclusive)
# the value is greater than 100
# the value is less than 0

def number_range(integer):
        if (integer < 0):
            print(f'{integer} is less than 0')
        elif (integer <= 50):
            print(f'{integer} is between 0 and 50')
        elif (integer <= 100):
            print(f'{integer} is between 51 and 100')
        else:
            print(f'{integer} is greater than 100')
            

number_range(0)     # 0 is between 0 and 50
number_range(25)    # 25 is between 0 and 50
number_range(50)    # 50 is between 0 and 50
number_range(75)    # 75 is between 51 and 100
number_range(100)   # 100 is between 51 and 100
number_range(101)   # 101 is greater than 100
number_range(-1)    # -1 is less than 0