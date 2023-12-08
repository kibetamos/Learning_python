#This programme determines whether a bank customer qualifies for a loan

min_salary = 20000
min_year = 2

#lets get customers annual salary
salary = float(input('Enter your annual salary: '))

#number of years on the current job

year_on_job = int(input('Enter the number of ' + 'years employed: '))

 # Determine whether the customer qualifies.
if salary >= min_salary or min_year >= min_year:
    print('You qualify for the loan.')
else:
    print('You do not qualify for this loan.')