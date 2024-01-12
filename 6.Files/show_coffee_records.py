# This program displays the records in the

def main():
    coffee_file = open('coffee.txt', 'r')

    descr = coffee_file.readline()

    while descr != '':
        qty = float(coffee_file.readline())

        #strip tjhe \n fro the sescriptiom

        descr = descr.rstrip('\n')

        #display the record
        print(f'Description: {descr}')
        print(f'Quantity: {qty}')

        descr = coffee_file.readline()

    coffee_file.close()

if __name__ == '__main__':
    main()