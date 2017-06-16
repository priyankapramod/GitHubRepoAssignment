from Hand import Hand
"""
Tests all the methods in class Hand.
"""
hand1 = Hand(13)
print(hand1)


print("***print for hand2.bjvalue***")
hand2 = Hand(7)
print(hand2.bjValue())


print("***print for hand3.hitme***")
hand3 = Hand(2)
hand3.hitMe()
print(hand3)

print("print for hand2 __str__method")
print(hand2.__str__())


"""
four of diamonds
two of diamonds
four of spades
Ace of diamonds
King of diamonds
eight of spades
nine of clubs
nine of diamonds
eight of spades
eight of spades
four of clubs
four of clubs
ten of hearts
***print for hand2.bjvalue***
46
***print for hand3.hitme***
four of clubs
Jack of hearts
Jack of spades
print for hand2 __str__method
two of clubs
eight of clubs
Jack of diamonds
eight of clubs
Queen of clubs
Ace of clubs
seven of spades

"""