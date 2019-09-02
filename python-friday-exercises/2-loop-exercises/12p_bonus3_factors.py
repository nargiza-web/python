# Bonus: Factor a Number
# Given a number, print its factors. What are factors? https://www.khanacademy.org/math/pre-algebra/factors-multiples/divisibility-and-factors/v/finding-factors-of-a-number
#----------------------------

value = int(input('Enter a number? '))
a = value+1
for i in range(1, a):
    if value % i == 0:
        print(i)