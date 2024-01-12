#Lets enable a user to edit/modify quantity

def main():
    #create a bool to use a flag found

    found = False

    #get the search value and new quantity

    search= input('Enter a description to search for : ')
    new_qty = int(input('Enter the new quantity: '))

    #open the original coffee.txt file
    coffee_file = open('coffee.txt', 'r')

    #open the temporary file
    temp_file = open('temp.txt', 'w')

    #Read the first records description field
    descr = coffee_file.readline()

    #Read the rest of teh file

    while descr !='':
        #Read the quantity field
        qty = float(coffee_file.readline())

        #strip \n from the description
        descr = descr.rstrip('\n')

        #write either this resord to the temporary file, 

        if descr == search:
            #write the modified record to the temp file
            temp_file.write(f'{descr}\n')
            temp_file.write(f'{new_qty}\n')

            #set the found flag to True

            found = True
        else:
            #write the original record tot te temp file
            temp_file.write(f'{descr}\n')
            temp_file.write(f'{qty}\n')

            

