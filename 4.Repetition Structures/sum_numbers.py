#calculate the sum of series of numbers
max = 5

#initialize accumulator variable
total = 0.0

#explanation
print('This program calculates the sum of ' , end='')

print(f'{max} numbers you will enter. ')

#get the numbers and accumulate them

for counter in range(max):
    number = int(input('Enter a number: '))
    total = total + number

    #lets show the total of the numbers

    print(f'The total is {total}. ')