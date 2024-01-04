# This program averages test scores. It asks the user for the
# number of students and the number of test scores per student.


# Get the number of students.
num_students = int(input('How many students do you have? '))

# Get the number of test scores per student.
num_test_scores = int(input('How many test scores per student? '))

# Determine each student's average test score.
for student in range(num_students):
    total = 0.0
    print(f'Student number {student + 1}')

    print('-----------------')

    for test_num in range(num_test_scores):
        print(f'Test number {test_num + 1}', end='')