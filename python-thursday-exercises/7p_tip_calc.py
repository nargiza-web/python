# 7. Tip Calculator
# Prompt the user for two things:
# The total bill amount:
# The level of service, which can be one of the following: good, fair, or bad
# Calculate the tip amount and the total amount (bill amount + tip amount). The tip percentage based on the level of service is based on:
# good -> 20%
# fair -> 15%
# bad -> 10%
# Example session: 
# $ python tip_calc.py 
# Total bill amount? 100 
# Level of service? good 
# Tip amount: $20.00 
# Total amount: $120.00 
# $ python tip_calc.py 
# Total bill amount? 48 
# Level of service? bad 
# Tip amount: $4.80 
# Total amount: $52.80
# Hints:
# To format a float number as a dollar value, use Python's formatting syntax: "{:.2f}".format(amount)
#-------------------------------------

bill= int(input('Total bill amount?'))
service = input ('Level of service?')
tip = 0
if service == 'good':
    tip = 0.2 * bill
elif service =='fair':
    tip = 0.15 * bill
elif service == 'bad':
    tip = 0.1 * bill
else :
    print ('type \'good\', \'fair\' or \'bad\' only')
print ('Tip amount: ${:.2f}'.format(tip))
total = tip + bill
print ('Total amount: ${:.2f}'.format(total))