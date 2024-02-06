# What happens when you run the following program? Why do we get that result?

# def set_foo():
#     foo = 'bar'

# set_foo()
# print(foo)

# On line 6, `set_foo()` is invoked and we temporarily jump into the body of the function `set_foo`. On line 4, `foo` is initialized to `bar` and then control is returned back to the caller on line 6, but since nothing was returned from the function, no value was captured into a variable. Then on line 7, the value `foo` is passed as an argument into the `print` invocation where an error is thrown because `foo` is recognized but out of scope.

# What does this program print? Why?

# foo = 'bar'

# def set_foo():
#     foo = 'qux'

# set_foo()
# print(foo)

# The code prints `bar` because it only access `foo` in the outer scope, not the `foo` variable in the function scope. The `foo` variable in the function also shadows the `foo` variable in the outer scope, blocking access to it. It cannot reassign the outer scoped `foo`.

# def multiply_numbers(num1, num2, num3):
#     result = num1 * num2 * num3
#     return result

# product = multiply_numbers(2, 3, 4)

# function name - `multiply_numbers` / on lines 1 and 5
# function arguments - `2`, `3`, `4`
# function definition - everything after `def` / everything on lines 1-3
# function body - lines 24, 25
# function parameters - `num1`, `num2`, `num3`
# function invocation - `multiply_numbers(2, 3, 4)`
# function return value - `product`, `result` / 24
# all identifiers - `multiply_numbers`, `result`, `num1`, `num2`, num3`, `product`

# What does the following code print?

# def scream(words):
#     return words + '!!!!'

# scream('Yipeee')

# 'Yipeee!!!!` / Nothing.

# What does the following code print?

# def scream(words):
#     words = words + '!!!!'
#     return
#     print(words)

# scream('Yipeee')


# Nothing. It also returns None.

# Without running the following code, what do you think it will do?

# def foo(bar, qux):
#     print(bar)
#     print(qux)

# foo('Hello')

# print 'Hello' / Raises an error because we've defined two parameters and only passed in one argument

# Without running the following code, what do you think it will do?

# def foo(bar, qux):
#     print(bar)
#     print(qux)

# foo(42, 3.141592, 2.718)

# raise a TypeError

# Without running the following code, what do you think it will do?

# def foo(first, second=3, third=2):
#     print(first)
#     print(second)
#     print(third)

# foo(42, 3.141592, 2.718)

# default values won't be used, it'll print all 3 arguments sequentially

# Without running the following code, what do you think it will do?

# def foo(first, second=3, third=2):
#     print(first)
#     print(second)
#     print(third)

# foo(42, 3.141592)

# 42, 3.141592, 2

# Without running the following code, what do you think it will do?

# def foo(first, second=3, third=2):
#     print(first)
#     print(second)
#     print(third)

# foo(42)

# 42, 3, 2

# Without running the following code, what do you think it will do?

# def foo(first, second=3, third=2):
#     print(first)
#     print(second)
#     print(third)

# foo()

# raise a TypeError, no args given and the first positional parameter needs a positional argument since it has no default value

# Without running the following code, what do you think it will do?

# def foo(first, second=3, third):
#     print(first)
#     print(second)
#     print(third)

# foo(42)

# raises a TypeError, third positional argument needed / raises a SyntaxError, when a positional parameter has a default value all subsequent positional parameters need default values

# Identify all of the identifiers on each line of the following code.

# def multiply(left, right): # multiply, left, right
#     return left * right # left, right

# def get_num(prompt): # get_num, prompt
#     return float(input(prompt)) # prompt, float, input

# first_number = get_num('Enter the first number: ') # first_number, get_num
# second_number = get_num('Enter the second number: ') # second_number, get_num
# product = multiply(first_number, second_number) # product, multiply, first_number, second_number
# print(f'{first_number} * {second_number} = {product}') # first_number, second_number, product, print

# Using the code below, classify the identifiers as global, local, or built-in. For our purposes, you may assume this code is the entire program.

# def multiply(left, right): # global
#     return left * right # local

# def get_num(prompt): # global
#     return float(input(prompt)) # built-in, local

# first_number = get_num('Enter the first number: ') # global, local
# second_number = get_num('Enter the second number: ') # global, local
# product = multiply(first_number, second_number) # global, local
# print(f'{first_number} * {second_number} = {product}') # built-in, global

# In the code shown below, identify all of the function names and parameters present in the code. Include the line numbers for each item identified.

# def multiply(left, right):
#     return left * right

# def get_num(prompt):
#     return float(input(prompt))

# first_number = get_num('Enter the first number: ')
# second_number = get_num('Enter the second number: ')
# product = multiply(first_number, second_number)
# print(f'{first_number} * {second_number} = {product}')

# multiply on lines 1 and 9
# left and right on line 1
# get_num on lines 4, 7, 8
# prompt on lines 4, 5
# / float, input, and print

# Which of the identifiers in the following program are function names? Which are method names? Which are built-in functions?

# def say(message):
#     print(f'==> {message}')

# string1 = input()
# string2 = input()

# say(max(string1.upper(), string2.lower()))

# function names - say
# method names - upper, lower
# built-ins - max, print, input 

# The following function returns a list of the remainders of dividing the numbers in numbers by 3:

# def remainders_3(numbers):
#     return [number % 3 for number in numbers]

# Use this function to determine which of the following lists contains at least one number that is not evenly divisible by 3 (that is, the remainder is not 0):

# numbers_1 = [0, 1, 2, 3, 4, 5, 6]
# numbers_2 = [1, 2, 4, 5]
# numbers_3 = [0, 3, 6]
# numbers_4 = []

# print(any(remainders_3(numbers_1)))
# print(any(remainders_3(numbers_2)))
# print(any(remainders_3(numbers_3)))
# print(any(remainders_3(numbers_4)))

# The following function returns a list of the remainders of dividing the numbers in numbers by 5:

def remainders_5(numbers):
    return [number % 5 for number in numbers]

# Use this function to determine which of the following lists do not contain any numbers that are divisible by 5:

numbers_1 = [0, 1, 2, 4, 5, 6, 7, 8, 9, 10]
numbers_2 = [1, 2, 3, 4, 6, 7, 8, 9]
numbers_3 = [0, 5, 10]
numbers_4 = []

print(all(remainders_5(numbers_1)))
print(all(remainders_5(numbers_2)))
print(all(remainders_5(numbers_3)))
print(all(remainders_5(numbers_4)))
