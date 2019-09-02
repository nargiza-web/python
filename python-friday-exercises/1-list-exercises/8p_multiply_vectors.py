# 8. Multiply Vectors
# Given two lists of numbers of the same length, create a new list by multiplying the pairs of numbers in corresponding positions in the two lists. Example:
# [2, 4, 5] x [2, 3, 6] = [4, 12, 30]
#---------------------------

numbers = [2, 4, 5]
number = [2, 3, 6]
list = []
for i in range(0, len(numbers)):
    number1 =number[i] * numbers[i]
    list.append(number1)

print (list)