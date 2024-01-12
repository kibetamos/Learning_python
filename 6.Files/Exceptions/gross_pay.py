#lets calculate th gross pay

def main():
    try:
        #lets get payrate
        pay_rate = float(input('Whats your pay rate '))

        #Lets add hours worked

        hours = int(input('How manuy hours have you worked '))

        #Grosspay
        gross_pay = hours * pay_rate

        print(f'Your Gross pay is {gross_pay:,.2f}')
    except ValueError:
        print('ERROR: Hours worked and hourly pay rate must be valid numbers.')


if __name__ == '__main__':
    main()