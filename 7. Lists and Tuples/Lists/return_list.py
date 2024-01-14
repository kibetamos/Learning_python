def main():
    numbers = get_values()

    # Display the values in the list.
    print('The numbers in the list are:')
    print(numbers)

def get_values():
    
    values = []

    #we have to create a loop and control it 
    again = 'y'

    #lets get the values from the user
    while again == 'y':
        num = int(input('Enter the value '))
        values.append(num)

        #do you want this again ?
        print('Do you want to add another number ? ')

        again = input('y = yes, anything else = no: ')
        print()

    return values

if __name__ == '__maina__':
    main()