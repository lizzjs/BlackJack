from Card import Card

class Hand:
    def __init__(self):
        self.cards = []

    #Checking which cards are in hand
    def __str__(self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card) + " "
        else:
            rep = "<empty>"
        return rep
    
    def add(self, card):
        self.cards.append(card)

# Testing: Add two cards to hand, check the value of J card
# card1 = Card('S', 4)
# card2 = Card('D', 'J')

# hand1 = Hand()
# hand1.add(card1)
# hand1.add(card2)
# print(hand1)
# print(card2.get_AJQK_value())
