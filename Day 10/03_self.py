class Employee:
    language = "Python" #This is a class attribute, shared by all instances of the class
    salary = 50000

    def getInfo(self):
        print(f"Language: {self.language}, Salary: {self.salary}")
ram= Employee()
ram.name = "Ram Kumar"
ram.language = "javascript" #This is an instance attribute, unique to this instance of the class
ram.getInfo()