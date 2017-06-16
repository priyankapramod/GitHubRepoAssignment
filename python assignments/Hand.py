import random
from RobustCardObject import Card


"""
File HandDoc
Defines class Hand and tests it by creating  Hand objects and calling methods on them.
"""
class Hand:
    """
    One object of class Hand represents one  set of cards which are
    equal to numCardsInHands.

    """

    suits = {"s": 'spades', "d": 'diamonds', "c":'clubs', "h": 'hearts'}
    ranks = {0:'',1:'Ace', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten', 11:'Jack', 12:'Queen', 13:'King'}
    suit = ""
    rank = 1

    def __init__(self, numCardsInHand):
        """
        sets Hand object with 'numCardsInHand' number of cards
        """
        self.myCards = list()
        for card in range(0,numCardsInHand):
            self.hitMe()





    def bjValue(self):
        """
        Returns the total black jack value of all the cards in the called Hand object
        """
        bjValue = 0
        for card in range(0,len(self.myCards)):
            bjValue += self.myCards[card].bj_value()

        return bjValue



    def __str__(self):
        """
        Returns a sentence that gives names of all cards in called Hand object
        """
        return '\n'.join(str(card) for card in self.myCards)


    def hitMe(self):
        """
        This method generates one card with random choice when called
        """
        suitlist = random.choice(list(self.suits.keys()))
        self.myCards.append(Card(random.randint(1,13),suitlist ))






