
from random import random


class Train():
    def book(self, trainNo, fro, to):
        print(f"Your ticket is booked for {trainNo}")
        print(f"From {fro} to {to}")

    def getStatus(self, trainName):
        print(f"Your train {trainName} is on time")

    def getFare(self, trainNo, fro, to):
        print(f"Your fare for {trainNo} from {fro} to {to} is {random.randint(100, 1000)}")

a = Train()
a.book("12345", "Delhi", "Mumbai")
a.getStatus("12345")
a.getFare("12345", "Delhi", "Mumbai")