class Employee:
    company = "TechCorp"
    def show(self):
        print(f"Employee: {self.name}, Salary: {self.salary}")
        
# class Programmer:
#     company = "TechCorp"
#     def show(self):
#         print(f"Programmer: {self.name}, Salary: {self.salary}, Language: {self.language}")

#     def show_language(self):
#         print(f"Programming Language: {self.language}")

class Programmer(Employee):
    company = "Apple"
    def showLanguage(self):
        print(f"The name is {self.name} and the programming language is {self.language}")

a=Employee()
b=Programmer()

print(a.company,b.company)