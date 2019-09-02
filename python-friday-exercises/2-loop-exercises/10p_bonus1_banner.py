# Bonus: Print a Banner
# Given a string, input by the user, print that string with a box around it. The box should stretch to the length of the string. Example session:
# $ python banner.py 
# Text? Welcome to DigitalCrafts 
# **************************** 
# * Welcome to DigitalCrafts * 
# ****************************
#----------------------

text = input('Text? ')
value = len(text)+2
star=''
print('*'*value)
print('*'+text+'*')
print('*'*value)


