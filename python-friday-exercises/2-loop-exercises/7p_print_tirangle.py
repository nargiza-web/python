# 7. Print a Triangle
# Print a triangle consisting of * characters like this:
#    * 
#   *** 
#  ***** 
# *******
#------------------------------

val = int(input('Enter the row? '))
m = (val*2)-2
for i in range (0, val):
    for j in range (0, m):
        print (end= " ")
    m -= 1
    for k in range (0, i+1):
        print ('*', end = " ")
    print(" ")

#ask magic about end?! when you delete 'end =' and leave the " " the result is not same? WHY?!!

