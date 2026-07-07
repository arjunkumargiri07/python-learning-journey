class Number:
    def __init__(self, n):
        self.n = n

    def __add__(self, num):
        return self.n + num.n

n= Number(10)
m= Number(20)

print(n + m)  # Output: 30