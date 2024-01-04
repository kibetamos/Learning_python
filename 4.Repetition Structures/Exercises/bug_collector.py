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