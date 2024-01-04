#PROBLEM STATEMENT
'''
1. Bug Collector
A bug collector collects bugs every day for five days. Write a program that keeps a running
total of the number of bugs collected during the five days. The loop should ask for the
number of bugs collected for each day, and when the loop is finished, the program should
display the total number of bugs collected.

'''
total = 0
max = 5



# Explain what we are doing.
print('This program calculates the sum of ', end='')
print(f'{max} numbers you will enter.') 

for counter in range(max):
    number = int(input('Enter a number: '))

    total = total+ number

#display sum of the numbers
print(f'The total is {total}')