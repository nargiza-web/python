# 3. Odd Numbers
# Print each odd number between 1 and 10 inclusive. Example output:
# $ python odd_numbers.py 
# 1 
# 3 
# 5 
# 7 
# 9
# Hint: you will need to use the modulus operator % to determine whether a number is odd or even.
#-----------------------

for i in range(1, 11):
    if i % 2 == 1:
        print(i)