# 7. Multiply a list
# Given a list of numbers, and a single factor (also a number), create a new list consisting of each of the numbers in the first list multiplied by the factor. Print this list.
#-------------------------------------------------------------------

numbers = [1, 2, 3, 5.6, 7.98, 4,5,6,7,89,10,6,7,90,34,12,78,98,54,571,33,99, -34, -43, -12, -3]
list_of_mult = []
for item in numbers: 
    list_of_mult.append(item * 3)
print (list_of_mult)