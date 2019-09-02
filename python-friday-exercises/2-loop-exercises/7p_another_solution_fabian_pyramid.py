# 7. Print a Triangle
# Print a triangle consisting of * characters like this:
#    * 
#   *** 
#  ***** 
# *******
#------------------------------

a = '*'
row = 20
column = 12
countdown = 0
for i in range(row):
    if i >= ((column//2)):  #checks the continuation of a symmetrical pyramid within given rows and columns
        break
    for j in range(column): 
        if j == ((column//2)): # checks if in the center of the # of columns
           pyramid = (' '*((column//2)-countdown))+(a*(2*(i+1)-1)) #equation
    countdown += 1        #part of equation
    print(pyramid)         #prints line by line 