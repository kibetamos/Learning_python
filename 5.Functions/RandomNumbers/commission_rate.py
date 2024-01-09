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

def get_sales():
    pass

def get_advanced_pay():
    pass
def determine_comm_rate(sale):
    pass