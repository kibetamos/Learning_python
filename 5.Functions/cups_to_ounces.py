#lets convert cupt to ounces

def main():
    #lets deisplay the introduction to the screen
    intro()
    cups = int(input('Enter the number of cups'))
    cups_to_ounces(cups)

#Introduction screen
def intro():
    print('This program converts measurements in cups to fluid ounces. For your')
    print('reference the formula is:')
    print(' 1 cup = 8 fluid ounces')
    print()

def cups_to_ounces(cups):
    ounces = cups * 8
    print(f'That converts to {ounces} ounces.')


main()