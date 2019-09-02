# 9. Matrix Addition
# Given two two-dimensional lists of numbers of the size 2x2 two dimensional list is represented as an list of lists:
# [ [2, -2], 
#   [5, 3] ]
# Calculate the result of adding the two matrices. The number in each position in the resulting matrix should be the sum of the numbers in the corresponding addend matrices. Example: to add
# 1 3 
# 2 4
# and
# 5 2 
# 1 0
# results in
# 6 5 
# 3 4
#---------------------------

matrix1 = [ 
    [1, 3],
    [2, 4]
]

matrix2 = [
    [5, 2],
    [1, 0]
]
result = [
    [0, 0],
    [0, 0]
]

for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        result[i][j] = matrix1[i][j] + matrix2[i][j]
print (result)
