#this programme allows the user search txt for records matchng the description

def main():
    #create a bool variable to use a flag

    found = False

    #lets get the search value

    search = input('Enter a description to search for ...')

    #lets open the file we want to search

    coffee_file = open('coffee.txt', 'r')

    ## Read the first record's description field.
    descr = coffee_file.readline()

    #lets read the rest of the file

    while descr != '':
        #read the quantity field

        qty = float(coffee.readline())

        #strip the \n from the descriotion

        descr = descr.rstrip('\n')

        #Determine whether this record matches the search value
        if descr == search:
            #display the record
            print(f'Description: {descr}')
            print(f'Quantity : {qty}')
            print()

            #Read the next description

        descr = coffee_file.readline()

    coffee_file.close()

    #if the search value was not found in the display message
    if not found:
        print('That item is not found in the file')

#call the main function
if __name__ == '__main__':
    main()
