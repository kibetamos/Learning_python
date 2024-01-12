#lets calculate th gross pay

def main():

    #lets get payrate
    pay_rate = float(input('Whats your pay rate'))

    #Lets add hpours worked

    hours = int(input('How manuy hours have you worked'))


    #Grosspay
    gross_pay = hours * pay_rate

    print(f'Your Gross pay is {gross_pay}')


if __name__ == '__main__':
    main()