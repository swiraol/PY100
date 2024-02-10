# String Formatting

# name = "Victor"
# profession = "programmer"

# msg_format = 'Hello {}. You are a {}.'
# formatted_msg = msg_format.format(profession, name)
# print(formatted_msg)
# print(f'Hello {name}. You are a {profession}.')

# In the following code snippet, find all violations of the PEP8 style guide. Rewrite it so that it conforms with the guide.

# ice_cream_density = 10

# while ice_cream_density > 0:
#     print('Drip...')
#     ice_cream_density -= 1

# print('The ice cream melted.')

# Find the Python Documentation on operator precedence, and use it to determine the result of evaluating 4 * 5 + 3**2 / 10.

# print((4 * 5) + ((3**2) / 10))
# print(((4 * 5) + (3**2)) / 10)

# Using the datetime module in Python, how would you obtain the current date and time?

# from datetime import datetime

# now = datetime.now()
# formatted_date = now.strftime("%a, %b %d at %I:%M %p")
# print(formatted_date)
# print(now)

# from datetime import date

# today = date.today()

# today_year = today.year
# print(today_year)
# iso_year = today.isocalendar()
# print(iso_year)

# the year attribute accesses the year attribute from `today`, which is a `date` object
# the isocalendar method provides 3 attributes and only the `year` attribute is accessed with bracket notation

# speed_limit = 60
# current_speed = 80

# if current_speed > speed_limit:
#     print('"People are so bad at driving cars that '
#           "computers don\'t have to be that good to be "
#           'much better." -- Marc Andreessen')

tweet = 'Woohoo! :-)'

if len(tweet) > 140:
    print('Tweet is too long!')

length_checker = len
length_of_tweet = length_checker(tweet + 5)