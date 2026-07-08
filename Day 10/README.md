# 📘 Chapter 10: Object-Oriented Programming (OOP)

This chapter introduces the fundamentals of **Object-Oriented Programming (OOP)** in Python. OOP is a programming paradigm that organizes code using **classes** and **objects**, making programs more modular, reusable, and easier to maintain.

---

## 📚 Topics Covered

- Introduction to Object-Oriented Programming
- Class
- Object
- Modelling a Problem Using OOP
- Class Attributes
- Instance Attributes
- `self` Parameter
- Static Methods
- `__init__()` Constructor

---

## 💡 What is Object-Oriented Programming?

Object-Oriented Programming (OOP) is a programming approach where problems are solved by creating **objects**.

### Advantages

- Promotes code reusability (DRY Principle)
- Makes code modular and organized
- Improves readability and maintainability
- Supports abstraction and encapsulation

---

## 🏛️ Class

A **class** is a blueprint used to create objects.

### Syntax

```python
class Employee:
    pass
```

A class can contain:

- Attributes (variables)
- Methods (functions)

---

## 🎯 Object

An **object** is an instance of a class.

When an object is created, memory is allocated, and the object can access all methods and attributes defined in its class.

### Example

```python
class Employee:
    pass

harry = Employee()
```

---

## 🧠 Modelling a Problem Using OOP

When designing a program using OOP:

| Concept | Example |
|---------|---------|
| Noun | Class (`Employee`) |
| Adjective | Attributes (`name`, `age`, `salary`) |
| Verb | Methods (`getSalary()`, `increment()`) |

---

## 🏢 Class Attributes

Class attributes belong to the class and are shared among all objects.

### Example

```python
class Employee:
    company = "Google"

harry = Employee()
print(harry.company)

Employee.company = "YouTube"
```

---

## 👤 Instance Attributes

Instance attributes belong to individual objects.

### Example

```python
harry.name = "Harry"
harry.salary = "30000"
```

### Attribute Lookup Order

Python checks for attributes in the following order:

1. Instance (Object)
2. Class

Instance attributes always take priority over class attributes.

---

## 👤 self Parameter

The `self` parameter refers to the current object of the class.

It is automatically passed whenever a method is called using an object.

### Example

```python
class Employee:
    company = "Google"

    def getSalary(self):
        print("Salary is not available")

harry = Employee()
harry.getSalary()
```

Equivalent to:

```python
Employee.getSalary(harry)
```

---

## ⚙️ Static Method

A static method does not require access to the object (`self`) or the class (`cls`).

Use the `@staticmethod` decorator.

### Example

```python
class Employee:

    @staticmethod
    def greet():
        print("Hello User")
```

Call it using:

```python
Employee.greet()
```

or

```python
harry.greet()
```

---

## 🏗️ `__init__()` Constructor

The `__init__()` method is a special constructor that is executed automatically when an object is created.

It is commonly used to initialize object attributes.

### Example

```python
class Employee:

    def __init__(self, name):
        self.name = name

    def getSalary(self):
        print("Salary is not available")

harry = Employee("Harry")
```

---

## ✨ Key Takeaways

- OOP organizes programs using classes and objects.
- A class acts as a blueprint for creating objects.
- Objects contain attributes and methods.
- Class attributes are shared by all objects.
- Instance attributes belong to individual objects.
- The `self` parameter refers to the current object.
- Static methods do not require object-specific data.
- The `__init__()` constructor initializes objects automatically.

---

## 🎯 Learning Outcome

After completing this chapter, you will be able to:

- Understand the principles of Object-Oriented Programming.
- Create classes and objects in Python.
- Differentiate between class and instance attributes.
- Use the `self` parameter effectively.
- Define and use static methods.
- Initialize objects using the `__init__()` constructor.

---

## 👨‍💻 Author

**Arjun Kumar Giri**

First-Year Computer Engineering Student  
Pokhara Engineering College

---

⭐ If you found this chapter helpful, consider giving the repository a star!
