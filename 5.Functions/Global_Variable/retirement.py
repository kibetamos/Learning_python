# we have a global constant to represent the contribution rate 
cont_rate = 0.05

def main():
    gross_pay = float(input('Enter your gros pay: '))
    bonus = float(input('Enter the amount of bonuses '))
    pay_contrib(gross_pay)
    bonus_contrib(bonus)

#pay_contrib accepts grosspay as an argument
def pay_contrib(gross):
    contrib= gross * cont_rate

    print(f'Contribution for gross pay: {contrib}')


def bonus_contrib(bonus):
    contrib = bonus*cont_rate

    print(f'Contribution for bonuses: {contrib}')

main()