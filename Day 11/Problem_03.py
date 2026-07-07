class Employee:
    salary = 230
    increment_salary = 20

    @property
    def salary_after_increase(self):
        return self.salary + (self.salary * self.increment_salary / 100)

    @increment_salary.setter
    def salary_after_increase(self, salary):
        self.increment_salary = (salary - self.salary) / self.salary * 100

e = Employee()
print(e.salary_after_increase)
print(e.increment_salary)  # Output: 20
