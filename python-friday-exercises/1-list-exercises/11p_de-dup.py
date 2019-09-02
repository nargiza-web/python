# 11. De-dup
# Given a list of numbers or strings, create a new list containing the same elements as the first list, except with any duplicate values removed. Print the list.
#---------------------------------------

de=[1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 8, 9, 123, 145, 147, 87, 3]
de = list(dict.fromkeys(de))
print (de)
