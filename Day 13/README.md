# 📘 Chapter 13: Advanced Python 2

This chapter explores advanced Python features that help developers write cleaner, more efficient, and maintainable code. It covers virtual environments, package management, lambda functions, string formatting, and functional programming techniques.

---

## 📚 Topics Covered

- Virtual Environment
- Installing Virtual Environments
- Pip Freeze & Requirements File
- Lambda Functions
- `join()` Method
- `format()` Method
- `map()`, `filter()`, and `reduce()`

---

# 🐍 Virtual Environment

A **Virtual Environment** is an isolated Python environment that allows you to install packages separately for different projects without affecting the system-wide Python installation.

### Benefits

- Keeps project dependencies isolated
- Prevents version conflicts
- Makes projects portable
- Easy collaboration with other developers

---

## ⚙️ Installing Virtual Environment

Install the `virtualenv` package using pip:

```bash
pip install virtualenv
```

---

## 📁 Creating a Virtual Environment

Create a new virtual environment:

```bash
virtualenv myprojectenv
```

---

## ▶️ Activating the Environment

### Windows

```bash
myprojectenv\Scripts\activate
```

### Linux / macOS

```bash
source myprojectenv/bin/activate
```

Once activated, the virtual environment works like a separate Python installation.

---

# 📦 Pip Freeze Command

The `pip freeze` command lists all installed packages along with their versions.

### Example

```bash
pip freeze
```

Save installed packages to a file:

```bash
pip freeze > requirements.txt
```

Install packages from the file:

```bash
pip install -r requirements.txt
```

This makes it easy to recreate the same development environment on another system.

---

# ⚡ Lambda Functions

A **Lambda Function** is an anonymous (nameless) function created using the `lambda` keyword.

### Syntax

```python
lambda arguments: expression
```

### Example

```python
square = lambda x: x * x

print(square(6))
```

Output

```
36
```

Another example:

```python
sum = lambda a, b, c: a + b + c

print(sum(1, 2, 3))
```

Output

```
6
```

---

# 🔗 `join()` Method

The `join()` method combines elements of an iterable into a single string.

### Example

```python
fruits = ["apple", "mango", "banana"]

result = ", ".join(fruits)

print(result)
```

Output

```
apple, mango, banana
```

---

# 📝 `format()` Method

The `format()` method inserts values into placeholders inside a string.

### Example

```python
print("{} is a good {}".format("Harry", "boy"))
```

Output

```
Harry is a good boy
```

Changing the order:

```python
print("{1} is a good {0}".format("boy", "Harry"))
```

Output

```
Harry is a good boy
```

---

# 🔄 `map()` Function

The `map()` function applies a function to every element of an iterable.

### Syntax

```python
map(function, iterable)
```

### Example

```python
numbers = [1, 2, 3, 4]

square = list(map(lambda x: x * x, numbers))

print(square)
```

Output

```
[1, 4, 9, 16]
```

---

# 🎯 `filter()` Function

The `filter()` function returns elements that satisfy a condition.

### Example

```python
numbers = [1, 2, 3, 4, 5, 6]

even = list(filter(lambda x: x % 2 == 0, numbers))

print(even)
```

Output

```
[2, 4, 6]
```

---

# ➕ `reduce()` Function

The `reduce()` function performs cumulative operations on elements of an iterable.

It is available in the `functools` module.

### Example

```python
from functools import reduce

numbers = [1, 2, 3, 4]

result = reduce(lambda x, y: x + y, numbers)

print(result)
```

Output

```
10
```

Reduction process:

```
1 + 2 = 3
3 + 3 = 6
6 + 4 = 10
```

---

## ✨ Key Takeaways

- Virtual environments isolate project dependencies.
- `pip freeze` creates a list of installed packages.
- `requirements.txt` simplifies project setup.
- Lambda functions create concise anonymous functions.
- `join()` combines iterable elements into a string.
- `format()` formats strings dynamically.
- `map()` transforms iterable elements.
- `filter()` selects elements based on conditions.
- `reduce()` performs cumulative computations.

---

## 🎯 Learning Outcome

After completing this chapter, you will be able to:

- Create and manage virtual environments.
- Share project dependencies using `requirements.txt`.
- Write anonymous functions with `lambda`.
- Manipulate strings using `join()` and `format()`.
- Apply functional programming concepts using `map()`, `filter()`, and `reduce()`.
- Write cleaner and more efficient Python code.

---

## 👨‍💻 Author

**Arjun Kumar Giri**

First-Year Computer Engineering Student  
Pokhara Engineering College

---

⭐ If you found this chapter helpful, consider giving the repository a star!
