# This program uses a dictionary as a deck of cards.
import random

def main():
    deck = create_deck()

    #get the number of cards to to deal
    num_cards = int(input('How many cards should I deal ?'))

    #deal cards
    deal_cards(deck, num_cards)



def create_deck():
    pass