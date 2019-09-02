# 10. How many coins?
# Write a program that will prompt you for how many coins you want. Initially you have no coins. It will ask you if you want a coin? If you type "yes", it will give you one coin, and print out the current tally. If you type no, it will stop the program. Example run:
# $ python coins.py 
# You have 0 coins. 
# Do you want another? yes 
# You have 1 coins. 
# Do you want another? yes 
# You have 2 coins. 
# Do you want another? no 
# Bye
#-------------------------------

coin = 0
print(f' You have {coin} coins ')
answer = input ('Do you want another?')

while answer == 'yes':
    coin += 1
    print (f'You have {coin} coins')
    answer = input ('Do you want another? ')
print ('Bye')