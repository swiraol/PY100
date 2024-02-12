# Write an if statement that prints Yes! if random_number is 1, and No. if random_number is 0.

# import random
# random_number = random.randint(0, 1)

# if random_number == 1:
#     print(random_number)
#     print('Yes!')
# else:
#     print(random_number)
#     print('No.')

# print('Yes' if random_number else 'No')

# Initialize a variable weather with a string value being 'sunny', 'rainy', or whatever weather condition you choose. Then, write an if statement that prints:

weather = 'eh'

# match weather:
#     case 'sunny':
#         print("It's a beautiful day!")
#     case 'rainy':
#         print("Grab your umbrella.")
#     case _:
#         print("Let's stay inside.")

if weather == 'sunny':
    print("It's a beautiful day!")
elif weather == 'rainy':
    print("Grab your umbrella.")
else:
    print("Let's stay inside.")

# It's a beautiful day! if weather's value is 'sunny'
# Grab your umbrella. if weather's value is 'rainy'
# Let's stay inside. if weather's value is anything else
# Test your code with different values for weather.