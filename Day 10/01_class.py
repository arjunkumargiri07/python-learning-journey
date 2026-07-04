class Employee:
    language = "Python" #This is a class attribute, shared by all instances of the class
    salary = 50000 #This is a class attribute, shared by all instances of the class

John = Employee()
John.name = "John Doe"
print(John.name, John.language, John.salary)

harry = Employee()
harry.name = "Harry Potter"
print(harry.name, harry.language, harry.salary)