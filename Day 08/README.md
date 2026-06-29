
# 📘 Python Programming Handbook

## Chapter 08 – Functions & Recursions

Beginner Friendly Learning Guide

---

## 📖 Overview

Functions are reusable blocks of code that perform a specific task. They help make programs more organized, modular, and easier to maintain.

Recursion is a programming technique where a function calls itself to solve a problem by breaking it down into smaller subproblems.

---

# 📚 Topics Covered

* Functions
* Function Definition
* Function Call
* Built-in Functions
* User-defined Functions
* Function Arguments
* Return Values
* Default Parameters
* Recursion
* Recursive Functions

---

# 🔹 What is a Function?

A **function** is a block of reusable code designed to perform a particular task.

Functions help:

* Reduce code duplication
* Improve readability
* Make programs modular
* Simplify debugging and maintenance

---

# 🔹 Function Syntax

```python
def function_name():
    # Function body
```

---

## 💻 Example

```python
def greet():
    print("Hello!")

greet()
```

### Output

```
Hello!
```

---

# 🔹 Function Definition

The **function definition** contains the statements that execute whenever the function is called.

```python
def greet():
    print("Good Day!")
```

---

# 🔹 Function Call

A **function call** executes the function.

```python
greet()
```

---

## 💻 Practice Example

Write a function to greet the user.

```python
def greet():
    print("Good Day!")

greet()
```

### Output

```
Good Day!
```

---

# 🔹 Types of Functions

Python provides two types of functions.

## 1. Built-in Functions

These are already available in Python.

Examples:

```python
print()
len()
range()
type()
input()
sum()
```

### Example

```python
numbers = [10, 20, 30]

print(len(numbers))
```

**Output**

```
3
```

---

## 2. User-defined Functions

These are created by the programmer.

```python
def welcome():
    print("Welcome to Python!")

welcome()
```

---

# 🔹 Functions with Arguments

Arguments allow information to be passed into a function.

### Example

```python
def greet(name):
    print("Hello", name)

greet("Harry")
```

### Output

```
Hello Harry
```

---

# 🔹 Returning Values

Functions can return values using the `return` keyword.

### Example

```python
def greet(name):
    return "Hello " + name

message = greet("Harry")

print(message)
```

### Output

```
Hello Harry
```

---

# 🔹 Default Parameter Values

A function parameter can have a default value.

If no argument is provided, the default value is used.

### Example

```python
def greet(name="Stranger"):
    print("Hello", name)

greet()
greet("Harry")
```

### Output

```
Hello Stranger
Hello Harry
```

---

# 🔹 Recursion

A **recursive function** is a function that calls itself.

It is commonly used to solve problems that can be divided into smaller, similar subproblems.

---

## 💻 Factorial Using Recursion

```python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))
```

### Output

```
120
```

---

# 🔹 How Recursion Works

For `factorial(5)`:

```
factorial(5)
= 5 × factorial(4)
= 5 × 4 × factorial(3)
= 5 × 4 × 3 × factorial(2)
= 5 × 4 × 3 × 2 × factorial(1)
= 5 × 4 × 3 × 2 × 1
= 120
```

---

# ⚠️ Important Notes on Recursion

* Every recursive function **must have a base case**.
* Without a base case, the function will call itself forever, causing a **RecursionError**.
* Recursion often provides elegant solutions but may use more memory than loops.

---

# 📝 Important Notes

* Functions improve code reusability.
* Use meaningful function names.
* Functions can accept zero or more arguments.
* `return` sends a value back to the caller.
* Default parameters make functions more flexible.
* Recursion is powerful but should always include a stopping condition.

---


---

# 🎯 Learning Outcomes

After completing this chapter, you will be able to:

* ✅ Create and call functions.
* ✅ Understand function definitions and function calls.
* ✅ Differentiate between built-in and user-defined functions.
* ✅ Pass arguments to functions.
* ✅ Return values from functions.
* ✅ Use default parameter values.
* ✅ Solve problems using recursion.


---
Author

Arjun Kumar Giri

Computer Engineering Student | Embedded Systems & IoT Enthusiast

GitHub: https://github.com/arjunkumargiri07

---

### ⭐ If you found this chapter helpful, consider giving the repository a star!
