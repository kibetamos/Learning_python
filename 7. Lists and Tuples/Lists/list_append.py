#Append is to add
# This program demonstrates how the append
# method can be used to add items to a list.

def main():
    #First, create an empty list
    name_list = []

    again = 'y'

    #create a variable to control the loop
    while again == 'y':
        #get a name from the user
        name = input('Enter a name: ')

        #append the name to the list
        name_list.append(name)

        #add another ?
        print('Do you want to add another name ?')
        again = input('y = yes, anything else = no: ')
        print()

    for name in name_list:
        print(name)

#call the main function
        
if __name__ == '__main__':
    main()

        