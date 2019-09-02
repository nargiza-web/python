# 10. Matrix Addition II
# Use your solution in Matrix Addition-9p_matrix_addition, and extend it to work for a pair of matrices of any size, as long as they have the same size.
#--------------------------------------------------

matrix1 = [[1,2,3,4,5,6,7,8],
           [1,2,3,4,5,6,7,8]]
matrix2 = [[1, 2, 3, 4, 5, 6, 7, 10],
           [1, 2, 3, 4, 5, 6, 7, 8]]

result=[[],[]]

for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        
        result[i].append(matrix1[i][j]+matrix2[i][j])
print(result)
        
