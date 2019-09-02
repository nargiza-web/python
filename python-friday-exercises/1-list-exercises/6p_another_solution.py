# 6. Positive Numbers II
# Given a list of numbers, create a new list which contains every number in the given list which is positive.
#----------------------------------------------------------

numbers = [1, 2, 3, 5.6, 7.98, 4,5,6,7,89,10,6,7,90,34,12,78,98,54,571,33,99, -34, -43, -12, -3]
new_list = []
for number in numbers :
    if number > 0 :
        new_list.append(number)
print (new_list)