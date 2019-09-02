# Bonus: Triangle Numbers
# Print the first 100 triangle numbers. What is a triangle number? Read this: https://www.mathsisfun.com/algebra/triangular-numbers.html.
#-----------------------

triangle = int (input('how many triangles?'))
result = 0
a = triangle+1

for i in range(1,a):
    result = i * (i+1)/2
    i += 1
    print (result)