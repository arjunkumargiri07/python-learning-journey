class Employee:
    a = 10

    @classmethod
    def show(cls):
      print(f"Employee class variable a: {cls.a}")

    @property 
    def name(self):
     return f"{self.fname} {self.lname}"

    @name.setter
    def name(self, value):
       self.fname = value.split(" ")[0]
       self.lname = value.split(" ")[1]

e = Employee()
e.a = 40

e.name = "John Ade"
print(e.name)

e.show()  # Output: Employee class variable a: 10