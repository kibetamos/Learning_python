#Allows a user delete s record in the coffee tt fie

import os

def main():
    found = False

    #get cofee to delete

    search = input('Which coffee do you want to delete? ')

    #open original coffee.txt file
    coffee_file = open('coffee.txt', 'r')

    #open temporary file
    temp_file = open('temp.txt', 'w')
    
    #Read the first records descrition fiel
    descr = coffee_file.readline()

    #lets read the rest of the file

    while descr != '':
#read quantity field
        qty = float(coffee_file.readline())

        descr = descr.rstrip('\n')

        if descr != search:
            temp_file.write(f'{descr}\n')
            temp_file.write(f'{qty}\n')
        
        else:
            found = True

        #read the next description

    descr = coffee_file.readine()

    coffee_file.close()
    temp_file.close()


    os.remove('coffee.txt')

    os.rename('temp.txt', 'coffee.txt')

    if found:
        
        print('The file has been updated.')
    else:
        print('That item was not found in the file.')

if __name__ == '__main__':

    main()