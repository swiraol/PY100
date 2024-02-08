# The following code causes an infinite loop (a loop that never stops iterating). Why?

# counter = 0

# while counter < 5:
#     print(counter)
#     counter += 1

# Write a program named age.py that includes someone's age and then calculates and reports the future age 10, 20, 30, and 40 years from now. Here's the output for someone who is 22 years old.

# You are 22 years old.
# In 10 years, you will be 32 years old.
# In 20 years, you will be 42 years old.
# In 30 years, you will be 52 years old.
# In 40 years, you will be 62 years old.

# solution 1

# ages = {'10': 32, '20': 42, '30': 52, '40': 62}
# print('You are 22 years old.')
# for key in ages:
#     print(f'In {key} years, you will be {ages[key]} years old.')

# solution 2

# age = int(input())
# print(f'You are {age} years old.')

# for future in range(10, 50, 10):
#     print(f'In {future} years, you will be {age + future} years old.')

# Use a while loop to print the numbers in my_list, one number per line. Then, do the same with a for loop.

# my_list = [6, 3, 0, 11, 20, 4, 17]

# index = 0
# while index < len(my_list):
#     print(my_list[index])
#     index += 1

# for num in my_list:
#     print(num)

# Use a while loop to print all numbers in my_list with even values, one number per line. Then, print the odd numbers using a ' for' loop.

# my_list = [6, 3, 0, 11, 20, 4, 17]

# index = 0
# while index < len(my_list):
#     if my_list[index] % 2 == 0:
#         even_number = my_list[index]
#         print(even_number)    
#     index += 1

# for num in my_list:
#     if num % 2 == 1:
#         odd_number = num
#         print(odd_number)    

# Print all of the even numbers in the following list of nested lists. Don't use any while loops.

# my_list = [
#     [1, 3, 6, 11],
#     [4, 2, 4],
#     [9, 17, 16, 0],
# ]

# for outer in my_list:
#     for inner in outer:
#         if inner % 2 == 0:
#             print(inner)

# Let's try another variation on the even/odd-numbers theme.

# We'll return to the simpler one-dimensional version of my_list. In this problem, you should write code that creates a new list with one element for each number in my_list. If the original number is an even, then the corresponding element in the new list should contain the string 'even'; otherwise, the element should contain 'odd'.

# my_list = [
#     1, 3, 6, 11,
#     4, 2, 4, 9,
#     17, 16, 0,
# ]

# solution 1 using for loop
# new_list = []
# for number in my_list:
#     if number % 2 != 0:
#         new_list.append('odd')
#     else:
#         new_list.append('even')
# print(new_list)

# solution 2 using list comprehension
# def even_or_odd(number):
#     return 'even' if number % 2 == 0 else 'odd'

# result = [even_or_odd(number) for number in my_list]
# print(result)

# Write a find_integers function that returns a list of all the integers from my_tuple:

# my_tuple = (1, 'a', '1', 3, [7], 3.1415,
#             -4, None, {1, 2, 3}, False)

# def find_integers(object):
#     result = []
#     my_list = list(object)
#     for element in my_list:
#         if isinstance(element, int) and not isinstance(element, bool):
#             result.append(element)
#     return result

# solution 2 

# def find_integers(object):
#     result = []
#     my_list = list(object)
#     for element in my_list:
#         if type(element) == int:
#             result.append(element)
#     return result

# solution 3 using list comprehension

# def find_integers(things):
#     result = [element for element in things if type(element) is int]
#     return result
# integers = find_integers(my_tuple)
# print(integers)    # [1, 3, -4]

# Write a comprehension that creates a dict whose keys are strings and whose values are the length of the corresponding key. Only keys with odd lengths should be in the dict. Use the set given by my_set as the source of strings.

# my_set = {
#     'Fluffy',
#     'Butterscotch',
#     'Pudding',
#     'Cheddar',
#     'Cocoa',
# }

# result = {key: len(key) for key in my_set if len(key) % 2 != 0}
# print(result)

# using a while loop

# def factorial(number):
#     result = 1
#     count = 1
#     while count <= number:
#         result *= count
#         count += 1
#     return result

# using a for loop

# def factorial(n):
#     result = 1
#     for number in range(n, 0, -1):
#         result *= number

#     return result

# print(factorial(1))   # 1
# print(factorial(2))   # 2
# print(factorial(3))   # 6
# print(factorial(4))   # 24
# print(factorial(5))   # 120
# print(factorial(6))   # 720
# print(factorial(7))   # 5040
# print(factorial(8))   # 40320
# print(factorial(25))  # 15511210043330985984000000

# The following code uses the randrange function from Python's math library to obtain and print a random integer within a given range. Using a while loop, it keeps running until it finds a random number that matches the last number in the range. Refactor the code so it doesn't require two different invocations of randrange.

# import random

# while number != highest:
#     number = random.randrange(highest + 1)
#     print(number)
# highest = 10
# while True:
#     # highest = 10
#     number = random.randrange(highest + 1)
#     print(number)
#     if number == highest:
#         break


# Print all of the even numbers in the following list of nested lists. This time, don't use any for loops.

my_list = [
  [1, 3, 6, 11],
  [4, 2, 4],
  [9, 17, 16, 0],
]

outer_index = 0
while outer_index < len(my_list):
    inner_index = 0
    while inner_index < len(my_list[outer_index]):
        number = my_list[outer_index][inner_index]
        if number % 2 == 0:
            print(number)

        inner_index += 1
    outer_index += 1
