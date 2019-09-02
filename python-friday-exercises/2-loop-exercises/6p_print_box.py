# 6. Print a Box
# Given a height and width, input by the user, print a box consisting of * characters as its border. Example session:
# $ python box.py Width? 6 Height? 4 
# ****** 
# *    * 
# *    * 
# ******
#---------------------------

width = int(input('Width?'))
height = int(input('Height'))

print ( '* ' * width)

for item in range(height-2):
    print('* ' + '  ' * (width-2) + '* ')
    item += 1
print ( '* ' * width)