class Employee:
    language = "Python" #This is a class attribute, shared by all instances of the class
    salary = 50000

ram= Employee()
ram.name = "Ram Kumar"
ram.language = "javascript" #This is an instance attribute, unique to this instance of the class
print(ram.name, ram.language, ram.salary) 