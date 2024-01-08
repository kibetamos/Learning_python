#lets work on key word arguments \\

def main():
    rate=0.01
    period=10
    principal=10000.0
    show_intrest(rate,period,principal)

def show_intrest(rate,period,principal):
    intrest = rate*period*principal

    print(f'The simple intrest will be {intrest}')

main()