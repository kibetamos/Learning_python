#lets calculate thw retail price

MARK_UP = 2.5 # The markup percentage
another = 'y' # Variable to control the loop

# Process one or more items.
while another == 'y' or another == 'Y':
    wholesale = float(input("Enter the item's wholesale cost: "))

    #lets calculate the retail price

    retail = wholesale * MARK_UP

    #display the retail price

    print(f'Retail price: ${retail:,.2f}')

    #lets do it again
    another = input('Do you have another item? ' +'(Enter y for yes): ')