def divisible5(n):
    if(n%5 == 0):
        return True
    return False

a = [1,23,44,5,645,68,79,580,90,96]

f= list(filter(divisible5, a))
print(f)