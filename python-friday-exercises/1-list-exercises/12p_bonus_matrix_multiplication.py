# Bonus: Matrix Multiplication
# Given two two-dimensional lists of numbers of the size 2x2 - calculate the result of multiplying the two matrices. Print the resulting matrix. How do you multiple two matricies? https://www.khanacademy.org/math/precalculus/precalc-matrices/multiplying-matrices-by-matrices/v/matrix-multiplication-intro
#----------------------------------

a = [ [2, 3], 
      [3, 4]]
b = [[1, 3], 
    [3, 0]]

result = [[],[]]

result[0].append( a[0][0] * b[0][0]+a[0][1]*b[1][0])
result[0].append(a[0][0]*b[0][1]+a[0][1]*b[1][1])
result[1].append(a[1][0]*b[0][0]+a[1][1]*b[1][0])
result[1].append(a[1][0]*b[0][1]+a[1][1]*b[1][1])
print(result)