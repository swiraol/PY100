# import random

# def predict_weather():
#     sunshine = random.choice([True, False])

#     if sunshine:
#         print("Today's weather will be sunny!")
#     else:
#         print("Today's weather will be cloudy!")

# print(predict_weather())

# When the user inputs 10, we expect the program to print The result is 50!, but that's not the output we see. Why not?

# def multiply_by_five(n):
#     return n * 5

# print("Hello! Which number would you like to multiply by 5?")
# number = int(input())

# print(f"The result is {multiply_by_five(number)}!")

# Magdalena has just adopted a new pet! She wants to add her new dog, Bowser, to the pets dictionary. After doing so, she realizes that her dogs Sparky and Fido have been mistakenly removed. Help Magdalena fix her code so that all three of her dogs' names will be associated with the key 'dog' in the pets dictionary.

# pets = { 'cat': 'pepe', 'dog': ['sparky', 'fido'], 'fish': 'oscar' }

# pets['dog'].append('bowser')

# print(pets)  # Output: {'cat': 'pepe', 'dog': 'bowser', 'fish': 'oscar'}

# def get_quote(person):
#     if person == 'Yoda':
#         return 'Do. Or do not. There is no try.'
#     if person == 'Confucius':
#         return 'I hear and I forget. I see and I remember. I do and I understand.'
#     if person == 'Einstein':
#         return 'Do not worry about your difficulties in Mathematics. I can assure you mine are still greater.'

# print(get_quote('Confucius'))

# print('Confucius says:')
# print('"' + get_quote('Confucius') + '"')

# You want to add the numbers from 1 to 5 to a list, but the code below is not producing the expected result. How can you fix it?

# numbers = []

# for i in range(1, 6):
#     numbers.append(i)

# print(numbers)

# info = {'name': 'Srdjan', 'age': 38}

# print(info.get('city', 'unknown'))
# print(info.get('name', 'unknown'))

# sub_list = ["-", "-", "-"]
# matrix = []

# # for _ in range(3):
# #     matrix.append(sub_list)
# # matrix[0] = ["X", "-", "-"]

# for _ in range(3):
#     matrix.append(sub_list[:])

# matrix[0] = "X"
# print(matrix) # [['X', '-', '-'], ['X', '-', '-'], ['X', '-', '-']]

# import math

# negative_infinity = -math.inf

# def find_maximum(numbers):
#     if not numbers:
#         return None
#     max_number = negative_infinity
#     for number in numbers:
#         if number > max_number:
#             max_number = number
#     return max_number

# print(find_maximum([45, 3, 10, 98, 22]))  # Expected 98
# print(find_maximum([-1, 0, 5, 3]))         # Expected 5
# print(find_maximum([-10, -3, -20, -2]))   # Expected -2

def digit_product(str_num):
    digits = [int(n) for n in str_num]
    product = 1

    for digit in digits:
        product *= digit

    return product

result = digit_product('12345')
print(result)  # expected: 120, actual: 0