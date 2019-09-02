# 5. Print a Square II
# Print a NxN square of * characters. Prompt the user for N. Example output:
# $ python square2.py How big is the square? 10 
# ********** 
# ********** 
# ********** 
# ********** 
# ********** 
# ********** 
# ********** 
# ********** 
# ********** 
# **********
# ----------------------------------------

value = int(input('How big is the square? '))
a = value + 1
star=''
j=0
while value < a:
    for i in range(value):
        star = '* '+star
    
        i += 1
    while j < value:
        print(star)
        j +=1
    value += 1