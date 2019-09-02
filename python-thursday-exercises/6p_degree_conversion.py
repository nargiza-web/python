# 6. Celsius to Fahrenheit
# Prompt the user for a number in degrees Celsius, and convert the value to degrees in Fahrenheit and display it to the user. Example session:
# $ python degree_conversion.py 
# Temperature in C? 
# 28 
# 82.4 F 
# $ python degree_conversion.py 
# Temperature in C? 
# -5 
# 23 F
# Hint: the formula to convert degrees C to degrees F is: F = C x 1.8 + 32.
#-----------------------------------------

celcius = int(input('Temperature in C?\n'))
fahrenheit = celcius * 1.8 + 32
print ('{:.2f}F'.format(fahrenheit))
