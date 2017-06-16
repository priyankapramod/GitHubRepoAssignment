import random


def coin_toss():
    head = 0
    tail = 0

    for count in range(0, 5000):
        print("Attempt #", count+1, ":", "Throwing a coin... ")
        toss = random.randint(1,2)
        if toss == 1:
            head = head + 1
        elif toss == 2:
            tail = tail + 1
        print("Got", head, "heads so far and ", tail, "tails so far")




coin_toss()