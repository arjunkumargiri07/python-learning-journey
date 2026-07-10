# 📘 Chapter 12: Advanced Python 1

This chapter introduces several modern and advanced Python features that make code more efficient, readable, and maintainable. These features were introduced in recent Python versions and are widely used in professional Python development.

---

## 📚 Topics Covered

- Walrus Operator (`:=`)
- Type Hints
- Advanced Type Hints
- Match-Case Statement
- Dictionary Merge & Update Operators
- Exception Handling
- Raising Exceptions
- `try...except...else`
- `try...finally`
- `if __name__ == "__main__"`
- Global Keyword
- Enumerate Function
- List Comprehensions

---

## 🦭 Walrus Operator (`:=`)

Introduced in **Python 3.8**, the Walrus Operator allows assigning a value while evaluating an expression.

### Example

```python
if (n := len([1, 2, 3, 4, 5])) > 3:
    print(f"List is too long ({n} elements)")
```

### Benefits

- Reduces repeated calculations
- Makes code shorter and cleaner
- Improves readability

---

## 📝 Type Hints

Type hints specify the expected data type of variables and function parameters.

### Variable Type Hint

```python
age: int = 25
```

### Function Type Hint

```python
def greeting(name: str) -> str:
    return f"Hello, {name}!"
```

---

## 🚀 Advanced Type Hints

The `typing` module provides advanced type annotations.

### Example

```python
from typing import List, Tuple, Dict, Union

numbers: List[int] = [1, 2, 3]

person: Tuple[str, int] = ("Alice", 30)

scores: Dict[str, int] = {
    "Alice": 90,
    "Bob": 85
}

identifier: Union[int, str] = "ID123"
```

### Common Types

| Type | Description |
|------|-------------|
| `List` | List of values |
| `Tuple` | Fixed collection of values |
| `Dict` | Key-value pairs |
| `Union` | Multiple possible data types |

---

## 🔀 Match-Case Statement

Introduced in **Python 3.10**, the `match` statement works similarly to the `switch` statement found in other programming languages.

### Example

```python
def http_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unknown Status"
```

---

## 📚 Dictionary Merge & Update Operators

Python allows dictionaries to be merged using the `|` operator.

### Example

```python
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

merged = dict1 | dict2

print(merged)
```

---

## 📂 Opening Multiple Files

Python allows multiple files to be opened using a single `with` statement.

### Example

```python
with (
    open("file1.txt") as f1,
    open("file2.txt") as f2
):
    pass
```

---

## ⚠️ Exception Handling

Exceptions help prevent program crashes by handling runtime errors.

### Example

```python
try:
    print(10 / 0)

except Exception as e:
    print(e)
```

### Handling Specific Exceptions

```python
try:
    pass

except ZeroDivisionError:
    pass

except TypeError:
    pass

except:
    pass
```

---

## 🚨 Raising Exceptions

Custom exceptions can be raised using the `raise` keyword.

### Example

```python
age = -5

if age < 0:
    raise ValueError("Age cannot be negative")
```

---

## ✅ Try with Else

The `else` block executes only if no exception occurs.

### Example

```python
try:
    print("Success")

except:
    print("Error")

else:
    print("Executed successfully")
```

---

## 🔒 Try with Finally

The `finally` block always executes, whether an exception occurs or not.

### Example

```python
try:
    print("Running")

finally:
    print("Always executes")
```

---

## ▶️ `if __name__ == "__main__"`

This statement checks whether the file is executed directly or imported as a module.

### Example

```python
if __name__ == "__main__":
    print("Running directly")
```

---

## 🌍 Global Keyword

The `global` keyword allows modification of a global variable inside a function.

### Example

```python
x = 10

def change():
    global x
    x = 20
```

---

## 🔢 Enumerate Function

The `enumerate()` function returns both the index and the value while iterating.

### Example

```python
names = ["Harry", "Rohan", "Shubham"]

for index, name in enumerate(names):
    print(index, name)
```

---

## ⚡ List Comprehensions

List comprehensions provide a concise way to create new lists from existing iterables.

### Example

```python
numbers = [1, 7, 12, 11, 22]

result = [item for item in numbers if item > 8]

print(result)
```

---

## ✨ Key Takeaways

- The Walrus Operator simplifies assignments inside expressions.
- Type hints improve code readability and maintainability.
- The `typing` module supports advanced type annotations.
- `match-case` provides a cleaner alternative to multiple `if-elif` statements.
- Dictionaries can be merged using `|`.
- Exception handling prevents unexpected program crashes.
- Custom exceptions can be created using `raise`.
- `else` and `finally` enhance exception handling.
- `__name__ == "__main__"` distinguishes scripts from imported modules.
- The `global` keyword modifies global variables.
- `enumerate()` provides indexes while looping.
- List comprehensions create lists efficiently with concise syntax.

---

## 🎯 Learning Outcome

After completing this chapter, you will be able to:

- Use modern Python syntax introduced in recent versions.
- Write cleaner code using the Walrus Operator.
- Apply type hints and advanced type annotations.
- Use `match-case` for pattern matching.
- Merge dictionaries efficiently.
- Handle and raise exceptions confidently.
- Understand the purpose of `__name__ == "__main__"`.
- Work with global variables when required.
- Iterate efficiently using `enumerate()`.
- Create powerful list comprehensions.

---

## 👨‍💻 Author

**Arjun Kumar Giri**

First-Year Computer Engineering Student  
Pokhara Engineering College

---

⭐ If you found this chapter helpful, consider giving the repository a star!

