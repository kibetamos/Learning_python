#lets take inputs of an exam 

# 1. Get the first test score.
# 2. Get the second test score.
# 3. Get the third test score.
# 4. Calculate the average by adding the three test scores and dividing the sum by 3.
# 5. Display the averag
math = float(input('What did you score in Math '))
eng = float(input('What did you score in English '))
swa = float(input('What did you score in Swahili '))
sci = float(input('What did you score in Science '))
average = (math + eng + swa + sci) / 4.0

print('Your result  score is ', average)

