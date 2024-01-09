#lets simulate a toss in coint 10 times

import random

#constants '
heads = 1
tails = 2
tosses = 2

#lets simulate the coin toss
def main():
    for toss in range(tosses):
        if random.randint(heads, tails) == tails:
            print('Tails')

        else:
            print('Heads')

#call main functions
            
main()