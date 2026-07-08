# 📘 Chapter 11: Inheritance & More on OOPs

This chapter introduces **Inheritance**, one of the core concepts of Object-Oriented Programming (OOP), along with advanced topics such as the `super()` method, class methods, property decorators, and operator overloading in Python.

---

## 📚 Topics Covered

- Inheritance
- Types of Inheritance
  - Single Inheritance
  - Multiple Inheritance
  - Multilevel Inheritance
- `super()` Method
- Class Methods
- `@property` Decorator
- Getter and Setter Methods
- Operator Overloading
- Magic (Dunder) Methods

---

## 🧬 Inheritance

Inheritance allows a new class (child class) to inherit the properties and methods of an existing class (parent class).

### Syntax

```python
class Employee:
    pass

class Programmer(Employee):
    pass
```

The child class can:
- Access methods and attributes of the parent class.
- Add new methods and attributes.
- Override existing methods.

---

## 🔹 Types of Inheritance

### 1. Single Inheritance

A child class inherits from one parent class.

```
Parent
   │
Child
```

---

### 2. Multiple Inheritance

A child class inherits from more than one parent class.

```
Parent 1     Parent 2
      \       /
       \     /
        Child
```

---

### 3. Multilevel Inheritance

A child class acts as the parent for another child class.

```
Parent
   │
Child 1
   │
Child 2
```

---

## 🚀 super() Method

The `super()` function is used to access the methods and constructor of the parent class.

### Example

```python
class Employee:
    def __init__(self):
        print("Employee Constructor")

class Programmer(Employee):
    def __init__(self):
        super().__init__()
        print("Programmer Constructor")
```

---

## 🏷️ Class Methods

Class methods belong to the class instead of its objects.

Use the `@classmethod` decorator.

### Example

```python
class Employee:
    company = "ABC"

    @classmethod
    def change_company(cls, name):
        cls.company = name
```

---

## 🏠 @property Decorator

The `@property` decorator allows a method to be accessed like an attribute.

### Example

```python
class Employee:
    @property
    def name(self):
        return self.ename
```

Usage:

```python
e = Employee()
print(e.name)
```

---

## ✏️ Getter and Setter

A **getter** retrieves a value, while a **setter** updates it.

### Example

```python
class Employee:
    @property
    def name(self):
        return self.ename

    @name.setter
    def name(self, value):
        self.ename = value
```

---

## ⚙️ Operator Overloading

Python allows operators to work with user-defined objects using special (dunder) methods.

| Operator | Magic Method |
|----------|--------------|
| `+` | `__add__()` |
| `-` | `__sub__()` |
| `*` | `__mul__()` |
| `/` | `__truediv__()` |
| `//` | `__floordiv__()` |

---

## ✨ Common Magic (Dunder) Methods

| Method | Purpose |
|---------|---------|
| `__str__()` | Returns a readable string representation of an object |
| `__len__()` | Defines the behavior of `len()` |
| `__add__()` | Overloads the `+` operator |
| `__sub__()` | Overloads the `-` operator |
| `__mul__()` | Overloads the `*` operator |

---

## 💡 Key Takeaways

- Inheritance promotes **code reusability**.
- Python supports **Single, Multiple, and Multilevel Inheritance**.
- `super()` is used to access members of the parent class.
- Class methods operate on the class rather than individual objects.
- `@property` provides controlled access to object attributes.
- Getter and Setter methods improve encapsulation.
- Operator overloading makes custom objects behave like built-in types.
- Magic methods customize the behavior of Python objects.

---

## 🎯 Learning Outcome

After completing this chapter, you will be able to:

- Implement different types of inheritance.
- Use `super()` to call parent constructors and methods.
- Create and use class methods.
- Implement properties using getters and setters.
- Overload operators for custom classes.
- Understand and use Python's magic methods effectively.

---

## 👨‍💻 Author

**Arjun Kumar Giri**

First-Year Computer Engineering Student  
Pokhara Engineering College

---

⭐ If you found this chapter helpful, consider giving the repository a star!
