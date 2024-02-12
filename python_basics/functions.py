# def multiply(num1, num2):
#     return num1 * num2

# print(multiply(12, 4))      # 48

# Write a function that prints Bruce Eckel's quote 'Python is executable pseudocode.'. What is the return value of the function?

# def bruce_eckel_quote():
#     print('Python is executable pseudocode.')

# bruce_eckel_quote()

# Let's generalize the function from the previous exercise. Implement a function named cite that takes two string arguments: the author of the quote and what they said. It then prints the quote, as shown below.

# def cite(author, quote):
#     print(f'{author} said: "{quote}"')

# cite('Bruce Eckel', 'Python is executable pseudocode.')
# Bruce Eckel said: "Python is executable pseudocode."

# Write a function that accepts a single argument, a number, and returns the result of multiplying its argument by an exponent of 2 (also known as squaring the number or raising the number to the power of 2).

# def squared_number(num):
#     return num**2

# print(squared_number(3))   # 9

# Write a function that compares the length of two strings. It should return -1 if the first string is shorter, 1 if the second string is shorter, and 0 if they're of equal length. For example:

# def compare_by_length(str1, str2):
#     if len(str1) < len(str2):
#         return -1
#     elif len(str2) < len(str1):
#         return 1
#     else:
#         return 0
    
# print(compare_by_length('patience', 'perseverance')) # -1
# print(compare_by_length('strength', 'dignity'))      #  1
# print(compare_by_length('humor', 'grace'))           #  0

# Use Python's string methods on the string 'Captain Ruby' to create a string with the value 'Captain Python'.

# def replace_string(str):
#     [one, two] = str.split()
#     replacement = two.replace(two, 'Python')
#     return f'{one} {replacement}'
    
# print(replace_string('Captain Ruby'))
# Use Python's control structures to create a function that takes an ISO 639-1 language code and returns a greeting in that language. You can take the examples below or add whatever languages you like.

def greet(language):
    match language:
        case 'en':
            return 'Hi!'
        case 'fr':
            return 'Salut!'
        case 'pt':
            return 'Olá!'
        case 'de':
            return 'Hallo!'
        case 'sv':
            return 'Hej!'
        case 'af':
            return 'Haai!'
        case _ :
            return 'Hi'

# print(greet('en'))         # Hi!
# print(greet('fr'))         # Salut!
# print(greet('pt'))         # Olá!
# print(greet('de'))         # Hallo!
# print(greet('sv'))         # Hej!
# print(greet('af'))         # Haai!
# print(greet(''))           # Hi!

# Write a function that extracts the language code from a locale. A locale is a combination of a language code, a region, and usually also a character set, e.g en_US.UTF-8.

def extract_language(locale):
    language_code = locale.split('_')
    return language_code[0]

# print(extract_language('en_US.UTF-8'))      # en
# print(extract_language('en_GB.UTF-8'))      # en
# print(extract_language('ko_KR.UTF-16'))     # ko

# Similar to the previous exercise, write a function that extracts the region code from a locale. For example:

def extract_region(locale):
    return locale[3:5]

# print(extract_region('en_US.UTF-8'))    # US
# print(extract_region('en_GB.UTF-8'))    # GB
# print(extract_region('ko_KR.UTF-16'))   # KR

def local_greet(locale):
    # if extract_region(locale) == 'US':
    #     return 'Hey!'
    # elif extract_region(locale) == 'GB':
    #     return 'Hello!'
    # elif extract_region(locale) == 'AU':
    #     return 'Howdy!'
    # else:
    #     return greet(extract_language(locale))
    region = extract_region(locale)
    language = extract_language(locale)

    match (region, language):
        case ('US', 'en'):
            return 'Hey'
        case ('GB', 'en'):
            return 'Hello'
        case ('AU', 'en'):
            return 'Howdy'
        case _:
            return greet(language)

print(local_greet('en_US.UTF-8'))       # Hey!
print(local_greet('en_GB.UTF-8'))       # Hello!
print(local_greet('en_AU.UTF-8'))       # Howdy!

print(local_greet('fr_FR.UTF-8'))       # Salut!
print(local_greet('fr_CA.UTF-8'))       # Salut!
print(local_greet('fr_MA.UTF-8'))       # Salut!