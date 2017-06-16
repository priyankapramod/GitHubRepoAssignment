__author__ = 'pksivar'





def factorial(positiveNum):
    fact = 1
    for x in range(1,positiveNum+1):
        fact = fact * x
    return  fact

print(factorial(5))