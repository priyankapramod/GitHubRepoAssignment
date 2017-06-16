from itertools import *


def make_dict(arr1, arr2):
    new_dict = {}
    for x in itertools.izip_longest(arr1,arr2):
        print(x)





    print(new_dict)

name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", ]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]


make_dict(name, favorite_animal)

