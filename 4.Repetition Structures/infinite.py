#lets demonstrate an infinite loop

#lets create a variable to control the loop

keep_going = 'y'

# Warning! Infinite loop!
while keep_going == 'y':

# Get a salesperson's sales and commission rate.
    sales = float(input('Enter the amount of sales: '))
    comm_rate = float(input('Enter the commission rate: '))

 # Calculate the commission.
    commission = sales * comm_rate

# Display the commission.
    print(f'The commission is ${commission:,.2f}.')