a = int(input("Enter a number: "))
b = int(input("Enter a second number :"))

if (b == 0):
    raise ZeroDivisionError("hey our program is not divise number by zero")

else:
    print(f"The division a/b is{a/b}")