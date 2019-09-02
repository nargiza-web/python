# FizzBuzz
# Write a program that outputs the string representation of numbers from 1 to n.
# But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.
# Expected Output:
# [
#    "1",
#    "2",
#    "Fizz",
#    "4",
#    "Buzz",
#    "Fizz",
#    "7",
#    "8",
#    "Fizz",
#    "Buzz",
#    "11",
#    "Fizz",
#    "13",
#    "14",
#     "FizzBuzz"
# ]
#------------------------------

val = int(input ('Enter a number ? '))
a = val+1
for i in range (1,a):
    if i % 3 == 0 and i % 5 == 0:
        print ('FizzBuzz')
        continue
    elif i % 3 == 0:
        print ('Fizz')
        continue
    elif i % 5 == 0:
        print ('Buzz')
        continue
    print (i)
    