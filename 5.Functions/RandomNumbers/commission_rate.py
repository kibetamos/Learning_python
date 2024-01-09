# This program calculates a salesperson's pay # at Make Your Own Music.

def main():
    sales = get_sales()

    #lets check the mount of advanced pay

    advanced_pay = get_advanced_pay()

    #determin e the commison rate
    comm_rate = determine_comm_rate(sales)

#lets calculate the pay
    pay = sales* comm_rate - advanced_pay
#Display the amount of pay
    print(f'The pay is ${pay:,.2f}.')

#Determine if the pay is negative 
    
    if pay < 0:
        print('The Salesperson must reimurse the company')

# The get_sales function gets a salesperson'sonthly sales
def get_sales():

    monthly_sales = float(input('Enter the monthly sales: '))
    return monthly_sales


def get_advanced_pay():
    # Get the amount of advanced pay.
    print('Enter the amount of advanced pay, or')
    print('enter 0 if no advanced pay was given.')
    
    advanced = float(input('Advanced pay: '))

    return advanced


def determine_comm_rate(sale):
    pass

