def temp(f):
    return 5*(f-32)/9

f=int(input("Enter temperature in Fahrenheit: "))
c=temp(f)
print("The temperature in Celsius is:", c)
