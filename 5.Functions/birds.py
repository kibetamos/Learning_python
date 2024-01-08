# This program demonstrates two functions that have local variables with the same name.

def main():

    texas()
    california()

#letys define the texas function
    
def texas():
    birds = 5000
    print(f'texas has {birds} birds')


#lets define the california function
    
def california():
    birds = 8000
    print(f'California has {birds} birds')


#call main function
    
main()