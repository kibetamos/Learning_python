high_score = 95


test1 = int(input('Enter the score for test 1: ' ))
test2 = int(input('Enter the score for test 2: ' ))
test3 = int(input('Enter the score for test 3: ' ))

# Calculate the average test score.
average = (test1 + test2 + test3) / 3

print(f'The average score is {average}.')

# If the average is a high score,
# congratulate the user.
if average >= high_score:
    print('Congratulations!')
    print('That is a great average!')