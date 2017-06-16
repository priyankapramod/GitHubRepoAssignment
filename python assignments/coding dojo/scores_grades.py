 # import random
# print(random.randint(0,9))
#
#
# random.randint(a, b)
# Score: 60 - 69; Grade - D
# Score: 70 - 79; Grade - C
# Score: 80 - 89; Grade - B
# Score: 90 - 100; Grade - A


import random

def rand_generator():
    temp = 0
    for count in range(0,10):
        temp = random.randint(60, 100)
        if temp >= 60 and temp <= 69:
            print("your score: ", temp , "Grade for your score is D")
        elif temp >= 70 and temp <= 79:
            print("your score: ", temp , "Grade for your score is C")
        elif temp >= 80 and temp <= 89:
            print("your score: ", temp , "Grade for your score is B")
        elif temp >= 90 and temp <= 100:
            print("your score: ", temp , "Grade for your score is A")


rand_generator()