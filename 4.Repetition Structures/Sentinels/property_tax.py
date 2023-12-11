#display property taxes

tax_factor = 0.0065

# Get the first lot number.
print('Enter the property lot number or enter 0 to end.')

lot = int(input('Lot number: '))

#continue processing as ong as the user does not enter 0

while lot !=0:
    #get the value of the property
    value = float(input('Enter the property value: '))

    #lets calculate the property tax
    tax = value * tax_factor

    #lets see the tax
    print(f'Property tax : ${tax:,.2f}')

    # Get the next lot number.
    print('Enter the next lot number or enter 0 to end.')
    lot = int(input('Lot number: '))



