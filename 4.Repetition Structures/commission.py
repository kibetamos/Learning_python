#calculate sales commissions
#lets create a variable to contol the loop
keep_going = 'y'

#calculate a series of commissions
while keep_going == 'y':
    # Get a salesperson's sales and commission rate
    sales = float(input('Enter the amount of sales: '))
    comm_rate = float(input('Enter the commission rate: '))

    # Calculate the commission.
    commission = sales * comm_rate

    # Display the commission
    print(f'The commission is ${commission:,.2f}.')

    # See if the user wants to do another one.
    keep_going = input('Do you want to calculate another ' + 'commission (Enter y for yes): ')
else:
    print("Kongoi for shopping with us ")
