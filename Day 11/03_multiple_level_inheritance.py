class Employee():
    a = 10

class Programmer(Employee):
    b = 12

class manager(Programmer):
    c =3

o = Employee()
p = Programmer()
m = manager()

print(o.a)
print(p.a, p.b)
print(m.a, m.b, m.c)