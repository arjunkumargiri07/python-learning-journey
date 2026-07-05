class Employee():
    def __init__(self):
        print("Employee Constructor")
    a = 10

class Programmer(Employee):
    def __init__(self):
        print("Programmer Constructor")
    b = 12

class manager(Programmer):
    def __init__(self):
        super().__init__()
        print("Manager Constructor")
    c =3

o = Employee()
p = Programmer()
m = manager()

print(o.a)
print(p.a, p.b)
print(m.a, m.b, m.c)