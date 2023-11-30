#we get items original price
#give a 20 % discount and show the sell price

original_price = float(input('Input the original price of the product'))
discount = original_price * 20/100


selling_price = original_price  - discount 


print('The Sale price of the product is ', selling_price)
