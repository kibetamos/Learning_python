import random 

min =1
max = 6

def main():
    #a variable to control the loop

    again = 'y'
    #lets roll the dice
    while again == 'y' or again == 'Y':
        print('Rolling the dice ...')
        print('Their values are ')
        print (random.randint(min,max))
        print (random.randint(min, max))

        #Another roll of the dice again?

        again = input('Roll them again ? (y = yes): ')

#call the main function
        
main()
