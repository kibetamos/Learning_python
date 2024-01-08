#define a function
def sum():
    #get  input from a user
    a = int(input('Enter a '))
#get second input from a user
    b = int(input('Enter b '))
#we call the second function which we have used to calculate the sum
    answer(a,b,sum)

#we define function 2 to do the sum
    #it takes in 3 parameters a,b and sum
def answer(a,b,sum):
    sum = a + b
    print ('The sum is,', sum)

#we call our function
sum()