#we are creating a file that add inventory to the coffee.txt file

def main():

    another = 'y'

    #open the coffee.txt file in append mode
    coffee_file = open('coffee.txt', 'a')

#add records to the file
    while another == 'y' or another == 'Y':
    
    #get coffee record data.
        print('Enter the followwing coffee data :')
        descr = input('Description: ')

        qty = int(input('Quantity (in pounds): '))

        #Append the data to the file
        coffee_file.write(descr + '\n')
        coffee_file.write(f'{qty} \n')


        # Determine whether the user wants to add
         # another record to the file.
        
        print('Do you want ot add another record ?')

        another = input('Y = yes, anything else = no: ')
    coffee_file.close()
    print('Data appended to coffee.txt.')


if __name__ == '__main__':
    main()