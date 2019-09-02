# 2. n to m
# Same as the previous problem, except you will prompt the user for the number to start on and the number to end on. Example session:
# $ python n_to_m.py Start from: 2 End on: 8 
# 2 
# 3 
# 4 
# 5 
# 6 
# 7 
# 8
#---------------------------

numbers = []
value_start = int(input('Start from: '))
value_end = int(input('End on: '))
value_end = value_end + 1
for i in range (value_start, value_end):
    print(i)
