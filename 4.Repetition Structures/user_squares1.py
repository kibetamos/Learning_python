#get users a loop to display a table of numbers and theirs sqaures

# Get the ending limit.
print('This program displays a list of numbers')
print('(starting at 1) and their squares.')

end = int(input('How high should I go? '))

# print the number and theri squares

for number in range(1, end + 1):
    square = number **2
    print(f'{number}\t{square}')
    