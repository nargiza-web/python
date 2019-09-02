# 8. Tip Calculator 2
# Allow the ability to divide the check into a equal parts amount a number of people. The user will enter the number of people to be divided amongst. Example session:
# $ python tip_calc2.py 
# Total bill amount? 100 
# Level of service? good 
# Split how many ways? 5 
# Tip amount: $20.00 
# Total amount: $120.00 
# Amount per person: $24.00
#--------------------------------------

bill= int(input('Total bill amount? '))
service = input ('Level of service? ')
split = int(input ('Split how many ways? '))
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
amount = total / split
print ('Amount per person: ${:.2f}'.format(amount))