# 8. Print a Triangle II
# Given a number as the height, print a triangle as in "Print a Triangle" but with the given height.
#----------------------------------------------

height = int(input('Enter the height of a triangle? '))
m = (height *2 )-2
for i in range (0, height):
    for j in range (0, m):
        print (end=" ")
    m -= 1
    for k in range (0, i+1):
        print ('*', end=" ")
    print (" ")
    
    #how they are same how they are different? 