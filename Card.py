class Card:
    #This class should initialize and return the suit and value for the cards
    def  __init__(self, suit, value):
        self.suit = suit
        self.value = value
        #Setting values for the Ace, Jack, Queen, King and numbcer cards
        if (value == 'A'):
            self.AJQK_value = 11
        elif value in ['J', 'Q', 'K']:
            self.AJQK_value = 10
        elif (value in ['2', '3', '4', '5', '6', '7', '8', '9', '10']):
            # value in [2, 3, 4, 5, 6, 7, 8, 9, 10]
            self.AJQK_value = int(value)

    def get_suit(self):
        return self.suit

    def get_value(self):
        return self.value    

    def get_AJQK_value(self):
        return self.AJQK_value

    #Add a def to view the format of the card
    def __str__(self):
        return "{}_{}".format(self.value, self.suit)


# Testing 
# card1 = Card('S', 4)
# # # print(card1.get_suit())
# print(card1)


