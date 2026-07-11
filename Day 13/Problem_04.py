from functools import reduce
a = [1,23,44,5,645,68,79,580,90,96]

def greater(a, b):
    if (a>b):
        return a
    return b

print(reduce(greater, a))