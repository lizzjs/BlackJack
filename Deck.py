from Card import Card
import random

class Deck:
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

    def __str__(self):
        print_deck = ''

        for i in range(len(self.cardsInDeck)):
            print_deck += self.cardsInDeck[i].__str__() + "\n"
        
        return f"This Deck has {str(len(self.cardsInDeck))} Cards.\nFour suits: Spades, Hearts, Diamonds and Clubs.\nAnd 13 cards for each suit. \n" + print_deck

    # will remove the card from the deck
    def deal_card(self):
        return self.cardsInDeck.pop(0) #deals the card on top

#Testing
deck1 = Deck()    
print(deck1.__str__())