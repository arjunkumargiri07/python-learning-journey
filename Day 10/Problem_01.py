class Programeer:
    comapany = "Microsoft"
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin

p = Programeer("Ram", 50000, 1234)
print(p.name, p.salary, p.pin, p.comapany)

r = Programeer("Rohan", 60000, 5678)
print(r.name, r.salary, r.pin, r.comapany)
