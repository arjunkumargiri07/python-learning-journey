n=int(input("Enter a number: "))
for i in range(1, n+1):
   product = 1
   for j in range(1, n+1):
        product *= j
print(f"Factorial of {i} is {product}")