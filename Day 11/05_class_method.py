class Employee:
    a = 10

    @classmethod
    def show(cls):
      print(f"Employee class variable a: {cls.a}")

e = Employee()
e.a = 40

e.show()  # Output: Employee class variable a: 10