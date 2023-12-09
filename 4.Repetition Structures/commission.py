#calculate sales commissions

#lets create a variable to contol the loop
keep_going = 'y'

#calculate a series of commissions
while keep_going == 'y':
    # Get a salesperson's sales and commission rate
    sales = float(input('Enter the amount of sales: '))
    comm_rate = float(input('Enter the commission rate: '))