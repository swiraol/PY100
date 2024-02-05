# Classify the following potential variable names as idiomatic, non-idiomatic, or illegal. For the non-idiomatic and illegal names, explain your choice.

# index # idiomatic
# CatName # idiomatic / Non-idiomatic - should not use uppercase letters
# lazy_dog # idiomatic
# quick_Fox # illegal because Fox is capitalized following an underscore / non-idiomatic - should not use uppercase letters
# 1stCharacter # non-idiomatic because it's neither PascalCase nor snakecase but digits are allowed / illegal - should not begin with a digit
# operand2 # illegal because there needs to be an underscore between operand and 2 / idiomatic
# BIG_NUMBER # idiomatic / non-idiomatic - should not use uppercase letters
# π # non-idiomatic because it's a special character / it's not an ASCII character

# Classify the following potential function names as idiomatic, non-idiomatic, or illegal. For the non-idiomatic and illegal names, explain your choice.

# index # non-idiomatic, starts with lowercase / idiomatic
# CatName # idiomatic / non-idiomatic
# lazy_dog # non-idiomatic, snake case / idiomatic
# quick_Fox # non-idiomatic, capitalized letter 
# 1stCharacter # illegal, starts with digit
# operand2 # non-idiomatic, no underscore / idiomatic
# BIG_NUMBER # non-idiomatic, all caps 
# π # non-idiomatic, special character

# functions follow the same rules as variables

# Classify the following potential constant names as idiomatic, non-idiomatic, or illegal. For the non-idiomatic and illegal names, explain your choice.

# index # non-idiomatic, lowercase letters
# CatName # non-idiomatic, Pascal case
# snake_case # non-idiomatic, snake-case
# LAZY_DOG3 # idiomatic
# 1ST # idiomatic / illegal, should not use digits as first character
# operand2 # non-idiomatic, lowercase
# BIG_NUMBER # idiomatic
# Π # non-idiomatic, special character / not an ASCII character

# Classify the following potential class names as idiomatic, non-idiomatic, or illegal. For the non-idiomatic and illegal names, explain your choice.

# index # non-idiomatic, lowercase letters
# CatName # idiomatic
# Lazy_Dog # non-idiomatic, underscore
# 1ST # non-idiomatic, all caps / illegal, should not begin with digit
# operand2 # non-idiomatic, lowercase
# BigNumber3 # idiomatic 
# Πi # non-idiomatic, no underscore / not an ASCII character

# Write a program named greeter.py that greets 'Victor' three times. Your program should use a variable and not hard code the string value 'Victor' in each greeting. Here's an example run of the program:

# Good Morning, Victor.
# Good Afternoon, Victor.
# Good Evening, Victor.

# name = 'Victor'
# print(f'Good Morning, {name}.')

# print ('Good Morning, ' + name + '.')

# Write a program named age.py that includes someone's age and then calculates and reports the future age 10, 20, 30, and 40 years from now. Here's the output for someone who is 22 years old.

# You are 22 years old.
# In 10 years, you will be 32 years old.
# In 20 years, you will be 42 years old.
# In 30 years, you will be 52 years old.
# In 40 years, you will be 62 years old.

# age = 22
# ten = 10
# twenty = 20
# thirty = 30
# fourty = 40

# print(f'You are {age} years old.')
# print(f'In {ten} years you will be {ten + age} years old.')
# print(f'In {twenty} years you will be {twenty + age} years old.')
# print(f'In {thirty} years you will be {thirty + age} years old.')
# print(f'In {fourty} years you will be {fourty + age} years old.')

# What happens when you run the following code? Why?

# age = 22
# print(f'You are {age} years old.')
# print(f'In 10 years, you will be {age + 10} years old.')
# print(f'In 20 years, you will be {age + 20} years old.')
# print(f'In 30 years, you will be {age + 30} years old.')
# print(f'In 40 years, you will be {age + 40} years old.')

# The code will print the intended values to the console. On lines 81-84, Python will first evaluate the two integer operands with the addition operator. It'll then run the string constructor function and coerce the passed in evaluated value to a string.

# What happens when you run the following code? Why?

# NAME = 'Victor'
# print('Good Morning, ' + NAME)
# print('Good Afternoon, ' + NAME)
# print('Good Evening, ' + NAME)

# NAME = 'Nina'
# print('Good Morning, ' + NAME)
# print('Good Afternoon, ' + NAME)
# print('Good Evening, ' + NAME)

# Python will throw an error because we're' attempting to reassign the constant variable `NAME` to `Nina`.

# Correction, Python will print `Victor` and `Nina` 3 times because Python doesn't have real constants.

# Assume you have $1,000.00 in the bank, and you've somehow managed to find a bank that pays you 5% (this is a wish-fulfillment fantasy) compounded interest every year. After one year, you will have $1,050 ($1,000 times 1.05). After two years, you will have $1,050 times 1.05, or $1102.50. Create a variable named balance that contains the amount of money you will have after 5 years, then print the result. Use a single expression if you can to set balance to the correct value.
# balance = 1000
# interest = 1.05
# print(((((balance * interest) * interest) * interest) * interest) * interest)

# Repeat the previous question but, this time, use augmented assignment to compute the final result, one year at a time.
# balance *= interest
# balance *= interest
# balance *= interest
# balance *= interest
# balance *= interest
# print(balance)

# Assume that obj already has a value of 42 when the code below starts running. Which of the subsequent statements reassign the variable? Which statements mutate the value of the object that obj references? Which statements do neither? If necessary, you can read the documentation.

obj = 'ABcd' # reassignment
obj.upper() # neither
obj = obj.lower() # reassignment
print(len(obj)) # neither
obj = list(obj) # reassignment
obj.pop() # mutated
obj[2] = 'X' # mutated
obj.sort() # mutated
set(obj) # neither
obj = tuple(obj) # reassignment