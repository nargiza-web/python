# 9. Multiplication Table
# Print the multiplication table for numbers from 1 up to 10. Example output:
# $ python multiplication_table.py 
# 1 X 1 = 1 
# 1 X 2 = 2 
# 1 X 3 = 3 
# 1 X 4 = 4 
# ... 
# 5 X 5 = 25 
# 5 X 6 = 30 
# 5 X 7 = 35 
# ... 
# 10 X 8 = 80 
# 10 X 9 = 90 
# 10 X 10 = 100
#----------------------------

for i in range (1,11):
    for j in range(1,11):
        result = i * j
        print (f'{i} X {j} = {result}')
        j += 1
    print ('---------------')
    i += 1