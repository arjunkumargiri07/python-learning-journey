class Employee:
    company = "TechCorp"
    name = "John Doe"
    salary = 50000
    def show(self):
        print(f"Employee: {self.name}, Salary: {self.salary}")
        
class Coder():
    language = "Python"
    def printLanguage(self):
        print(f"The programming language is {self.language}")

class Programmer(Employee,Coder):
    company = "Apple"
    def showLanguage(self):
        print(f"The name is {self.company} and the programming language is {self.language}")

a=Employee()
b=Programmer()
c=Coder()

b.show()
b.printLanguage()
b.showLanguage()