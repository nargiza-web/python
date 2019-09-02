# exercise 4. Day of the Week
# Given the following code that prompts the user for a day number (the int function converts a numeric string to a number):
# day = int(input('Day (0-6)? ')) # Fill in your code here
# The user will enter a number between 0 to 6 inclusive. Given this number, print a day of the week. 0 for Sunday, 1 for Monday, 2 for Tuesday, and so on. Here's an example user session (this assumes you've named the file day_of_week.py):
# $ python day_of_week.py 
# Day (0-6)? 5 
# Friday 
# $ python day_of_week.py Day (0-6)? 
# 0 
# Sunday
# ---------

day = int(input('Day (0-6)? '))
if day==0:
    print ('Sunday')
elif day==1:
    print ('Monday')
elif day==2:
    print ('Tuesday')
elif day==3:
    print ('Wednesday')
elif day==4:
    print ('Thursday')
elif day==5:
    print ('Friday')
elif day==6:
    print ('Saturday')
else:
    print('wrong')