#this program contains a class called cards where
#all the values of the particular card which calls  gets assigned.



__author__ = 'priyanka'

""" In file CardObjects.py. One object of  class Card stores one
    Cards's rank and suit and value.
"""

class Cards:


    Suits = {"s": 'spades', "d": 'diamonds', "c":'clubs', "h": 'hearts'}
    ranks = {0:'',1:'Ace', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten', 11:'Jack', 12:'Queen', 13:'King'}

    suit = ""
    rank = 1


#this is the basic constructor. Here  the current card's rank, suit values get assigned
#as per the parameters
    def __init__ (self, rank, suit):
        print ('constructing a Card object')
        for keys in self.ranks:
            if keys == rank:
                self.rank = rank
        self.suit = self.Suits[suit]


#get_rank(self) method when called by an instance object returns the card's rank value
    def get_rank(self):
        print (self.ranks[self.rank])
        return self.ranks[self.rank]

#get_suit(self) method when called by an instance object returns the card's suit value
    def get_suit(self):
        return self.suit


#bj_value (self) method when called by an instance object assigns particular black jack value
#  to the current card depending on its rank and returns card's black jack value
    def  bj_value(self):
         if self.rank < 10:
              return self.rank
         else:
              return 10




#the __str__( ) method is used to convert a Card object
# into a string

    def __str__(self):
        return self.ranks[self.rank] + " of " + self.suit





#test program
card1 = Cards(5, "d")
print(card1.__str__())

card2 = Cards(11, "s")
print(card2)

card3 = Cards(13, "h")
print(card3.get_rank())

card4 = Cards(1, "c")
print(card4)

print(card4.get_rank())
print(card2.bj_value())
print(card3.bj_value())




"" """"
constructing a Card object
five
constructing a Card object
Jack of spades
constructing a Card object
hearts
constructing a Card object
Ace of clubs
1
10
10
"" """