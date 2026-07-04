class Calculator:
    def __init__(self,n):
        self.n = n

    def square(self):
        print(f"The sqaure is {self.n*self.n}")

    def cube(self):
        print(f"The cube is {self.n*self.n*self.n}")

    def squareroot(self):
        print(f"The sqaure is {self.n**0.5}")

    @staticmethod
    def hello():
        print("Hello, I am a static method")

a = Calculator(4)
a.square()
a.cube()
a.squareroot()
a.hello()