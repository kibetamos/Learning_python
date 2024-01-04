#Calculate the sum of seriers of numbers entered by the user]]


max = 5

total = 0.0

# Explain what we are doing.
print('This program calculates the sum of ', end='')
print(f'{max} numbers you will enter.')

#get the number and accumukate them 

for counter in range(max):
    number = int(input('Enter a number: '))

    total = total+ number


#display sum of the numbers
print(f'The total is {total}')