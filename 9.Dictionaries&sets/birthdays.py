#python programe to keep friends birthdates 

#global constants
look_up = 1
add = 2
change = 3
delete = 4
quit = 5

#main function
def main():
    birthdays = {}
    
    # Initialize variable for the users choice
    choice = 0

    while choice != quit:
        #Get users menu choice

        choice = get_menu_choice()

        #process the choice
        if choice == look_up:
            look_up(birthdays)
        elif choice == add:
            add(birthdays)
        elif choice == change:
            change(birthdays)
        elif choice == delete:
            delete(birthdays)
        
# The get_menu_choice function displays the menu
# and gets a validated choice from the user
def get_menu_choice():
    print()
    print('Friends and Their Birthdays')
    print('---------------------------')
    print('1. Look up a birthday')
    print('2. Add a new birthday')
    print('3. Change a birthday')
    print('4. Delete a birthday')
    print('5. Quit the program')

    print()


    #Get the users choice

    choice = int(input('Enter your choice: '))

    # Validate the choice.
    while choice < look_up or choice > quit:
        choice = int(input('Enter a valid choice: '))

    # return the users choice 

    return choice     

def look_up(birthdays):
    name = input('Enter a name: ')
    
    #look it upa dictionary
    print(birthdays.get(name, 'Not found.'))

#the add functionadds a new entry into the birthdays dictioanry
    
def add(birthdays):
    #get name and birthdays
    name = input('Enter a name: ')
    bday = input('Enter a birthday: ')


    # If the name does not exist, add it.
    if name not in birthdays:
        birthdays[name] = bday
        print(f'Entry added: {name} - {bday}')
    else:
        print('That entry already exists.')

def delete(birthdays):
    #get name to looup
    name = input('Enter a name')
    ## If the name is found, delete the entry.

    if name in birthdays:
        del birthdays[name]
    else:
        print('That name is not found.')


#call the main function
        
if __name__ == '__main__':
    main()