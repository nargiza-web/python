# EXERCISE 2
# 2. HELLO, YOU!

# Same as the first exercise, but this time print the user's name in ALL CAPS, and also tell them the number of letters in their name. Example session:

# $ python hello2.py 
# WHAT IS YOUR NAME? Toby 
# HELLO, TOBY! 
# YOUR NAME HAS 4 LETTERS IN IT! AWESOME!
 

new_name = input('WHAT IS YOUR NAME? ')
new_name = new_name.upper()
print (f' HELLO, {new_name}!')
count = len(new_name)
print (f'YOUR NAME HAS {count} LETTERS IN IT! AWESOME!')
