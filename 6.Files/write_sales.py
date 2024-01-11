#prompt user for sales amoints anmd write them in a sales txt file 

def main():

    #lets get the number of days
    num_days = int(input('For how many days do you have sales'))

    #open a new fie names sales.txt

    sales_file = open('sales.txt', 'w')

    #Get each days sales and write it to the file
    for count in range(1, num_days +1):

        sales = float(f'Enter the sales for day #{count}: ')
        sales_file.write(f'{sales}\n')

    # Close the file.
    sales_file.close()

    print('Data written to sales.txt.')

if __name__ == '__main__':
    main()