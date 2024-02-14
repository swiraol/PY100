# Determine the length of the string "These aren't the droids you're looking for.".

# print(len("These aren't the droids you're looking for."))

# Convert the string 'confetti floating everywhere' to all upper case.


# print('confetti floating everywhere'.upper())

# Using the following code, compare the value of name with the string 'RoGeR' while ignoring the case of both strings. Print true if the values are the same; print false if they aren't. Next, perform a case-insensitive comparison between the value of name and the string 'DAVE'.

# name = 'Roger'

# print(name == 'RoGer'.title())
# print(name == 'DAVE')

# How can you assign the following rhyme to a single variable while preserving the line break?

# rhyme = '''A pirate I was meant to be!
# Trim the sails and roam the sea!'''

# rhyme = 'A pirate I was meant to be!\nTrim the sails and roam the sea!'

# print(rhyme)

# char_sequence = 'TkgaG92ZJjcmFmdCBpcyBmdWsIG9mIGVlbHMux'

# print('X'.casefold() in char_sequence)

# def check_for_x(str):
#     for char in str:
#         if char.casefold() == 'x':
#             return True
#     return False

# print(check_for_x(char_sequence))

# Write a function that checks whether a string is empty or not. For example:

# def is_empty(str):
#     # return len(str) == 0
#     return not str
# print(is_empty('mars'))  # False
# print(is_empty('  '))    # False
# print(is_empty(''))      # True

# Write an is_empty_or_blank function to determine whether a string is either empty or consists entirely of spaces. For example:

# def is_empty_or_blank(string):
#     return not string or string.isspace()

# print(is_empty_or_blank('mars'))  # False
# print(is_empty_or_blank('  '))    # True
# print(is_empty_or_blank(''))      # True

# Write code that capitalizes the words in the string 'launch school tech & talk', so that you get the string 'Launch School Tech & Talk'.

# def capitalize_words(string):
#     list_of_words = string.split(' ')
#     result = ''
#     index = 0
#     for word in list_of_words:
#         result += word.capitalize()
#         if (index == len(list_of_words) - 1):
#             break
#         else:
#             result += ' '
#         index += 1
#     return result

# def capitalize_words(string):
#     list_of_words = string.split(' ')
#     result = []
#     for word in list_of_words:
#         result.append(word.capitalize())
#     return ' '.join(result)

# def capitalize_words(string):
#     return string.title()

# print(capitalize_words('launch school tech & talk'))

# def starts_with(string1, string2):
#     for i in range(len(string2)):
#         if i >= len(string1) or string2[i] != string1[i]:
#             return False
        
#     return True

# print(starts_with("launch", "la"))   # True
# print(starts_with("school", "sah"))  # False
# print(starts_with("school", "sch"))  # True

# Write a function that counts the number of occurrences of a substring in a string.

# def count_substrings(string1, string2):
#     return string1.count(string2)

def count_substrings(string, substring):
    # Step 1: Initialize the counter
    count = 0
    
    # Step 2: Calculate the length of the substring
    substring_length = len(substring)
    print(substring_length) # 3
    
    # Step 3: Iterate over the string
    for i in range(len(string) - substring_length + 1): # 0, 1, 2, 3
        # Step 4: Slice the string
        if string[i:i+substring_length] == substring: # 0:3, 1:4, 2:5, 3:6
            # Step 5: Increment the counter if the substring matches
            count += 1
            
    # Step 6: Return the count
    return count
        
print(count_substrings("string", "ing")) # 1
# print(count_substrings("lemon lemon lemon", "lemon")) # 3
# print(count_substrings("laLAlaLA", "la")) # 2
# print(count_substrings("launch", "uno")) # 0