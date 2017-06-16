


__author__ = 'priyanka'


"""
File RobustCardObjectDoc
Defines class Card and tests it by creating  Card objects and calling methods on them.
"""

class Card:
    """
    One object of class Card represents one   card.
    """

    suits = {"s": 'spades', "d": 'diamonds', "c":'clubs', "h": 'hearts'}
    ranks = {0:'',1:'Ace', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten', 11:'Jack', 12:'Queen', 13:'King'}

    suit = ""
    rank = 1



    def __init__ (self, rank, suit):
        """
        sets Card object with its rank and suit value passed by the client as parameters.
        """

        if type(rank) != int:
            raise TypeError("type of the rank should be integer.")
        if  type(suit) != str:
            raise  TypeError("type of the suit should be a single character string")
        if  rank not in self.ranks.keys():
            raise  ValueError("value of the rank should be between 1 to 13")
        if  suit not in self.suits.keys():
            raise ValueError("value of suit should be one of the values in ('c','s','d','h')  ")
        for keys in self.ranks:
            if keys == rank:
                self.rank = rank
        self.suit = self.suits[suit]







    def get_rank(self):
        """
        Returns rank of the Card object instantiated.
        """
        return self.ranks[self.rank]


    def get_suit(self):
        """
        Returns suit value of Card object instantiated
        """
        return self.suit



    def  bj_value(self):
        if self.rank < 10:
            return self.rank
        else:
            return 10

        """
        Returns the  black jack value of  the card  instantiated
        """




    def __str__(self):
        """
        Returns a sentence that tells rank and suit values of the card object.
        """
        return self.ranks[self.rank] + " of " + self.suit








if __name__ == "__main__":
    try:

        card1 = Card(14, "s")
        print(card1.bj_value())

    except (ValueError, TypeError) as error:
        print (error)


    try:

        card2 = Card(12, "k")
        print(card2.__str__())

    except (ValueError, TypeError) as error:
        print (error)


    try:
        char = 'h'
        card3 = Card('h', "d")
        print(card3.bj_value())

    except (ValueError, TypeError) as error:
        print (error)


    try:

        card4 = Card(5, 6)
        print(card4)

    except (ValueError, TypeError) as error:
        print (error)


    try:

        char = 'l'
        card5 = Card('l', "c")
        print(card5.get_suit())


    except (ValueError, TypeError) as error:
        print (error)


    try:

        card6 = Card(11, ["c"])
        print(card6.__str__())

    except (ValueError, TypeError) as error:
        print (error)



    try:

        card7 = Card(13, "p")
        print(card7.get_rank())

    except (ValueError, TypeError) as error:
        print (error)



    try:

        card8 = Card(3, "h")
        print(card8)

    except (ValueError, TypeError) as error:
        print (error)







"" """"
value of the rank should be between 1 to 13
value of suit should be one of the values in ('c','s','d','h')
type of the rank should be integer.
type of the suit should be a single character string
type of the rank should be integer.
type of the suit should be a single character string
value of suit should be one of the values in ('c','s','d','h')
value of the rank should be between 1 to 13
"" """