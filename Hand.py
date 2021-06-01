from Card import Card

class Hand:
    def __init__(self):
        self.cards = []

    #Checking which cards are in hand
    def __str__(self):
        if self.cards:
            rep_hand = ""
            for card in self.cards:
                rep_hand += str(card) + " "
        else:
            rep_hand = "<empty>"
        return rep_hand
    
    def add(self, card):
        self.cards.append(card)

    def calculate_hand(self):
        self.value = 0
        ace_bool = False

        for card in self.cards:
            if card.value.isnumeric():
                self.value += int(card.value)
            else:
                if card.value == 'A':
                    ace_bool = True
                    self.value += 11
                else:
                    self.value += 10

        if ace_bool and self.value>21:
            self.value -= 10 #make Ace = 1 instead

        
    def get_value(self):
        self.calculate_hand()
        return self.value


# Testing: Add two cards to hand, check the value of A card
# card1 = Card('S', '4')
# card2 = Card('D', 'A')

# hand1 = Hand()
# hand1.add(card1)
# hand1.add(card2)
# print(hand1)
# # print(card2.get_Cardvalue())
# # print(card2.get_AJQK_value()) #might be redundant, comment out values in Card class
# print(hand1.get_value())
