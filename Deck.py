import Card
import random

class Deck(Card):
#This class should create the 52 card deck, deal, keep track of deck, and remove dealt cards
    def __init__(self):
        cardsInDeck = []
        suits = ['S', 'H', 'D', 'C']
        card_value = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    # will create 13 cards for each suit and store in cardsInDeck array
        for suit in suits:
            for value in card_value:
                cardsInDeck.append(Card(suit, value))
            
        self.cardsInDeck = cardsInDeck[:]

    # will shuffle the deck
    def shuffle_Deck(self):
        shuffle(self.cardsInDeck)

    # will remove the card from the deck
    def deal_card(self):
        return self.cardsInDeck.pop()

    
