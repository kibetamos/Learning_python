#global variable 
discount_percentage = 0.20

#main function
def main():

    #get items regualr price
    reg_price = get_regular_price()

#calculate the sale price 
    sale_price = reg_price - discount(reg_price)

    #Display  the sale price
    print(f'The sale price id {sale_price: ,.2f}')

    #lets get regular price fromthe user
def get_regular_price():
        price = float(input('Enter the Items Regular Price ' ))
        return price
    
def discount(price):
     return price * discount_percentage

#call main function
main()