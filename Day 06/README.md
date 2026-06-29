# 📘 Python Programming Handbook
## Chapter 06 – Conditional Expressions

Beginner Friendly Learning Guide

---

## 📖 Overview

Conditional expressions allow a Python program to make decisions based on specific conditions.

Just like in real life:

- 🎮 Play PUBG if it is Sunday.
- 🍦 Order ice cream if the weather is sunny.
- 🥾 Go hiking if your parents allow.

Similarly, Python executes different blocks of code depending on whether a condition is **True** or **False**.

---

# 📚 Topics Covered

- if Statement
- if...else Statement
- elif Statement
- Relational Operators
- Logical Operators
- Decision Making
- Practical Examples

---

# 🔹 The `if`, `elif`, and `else` Statements

Python uses conditional statements to execute different code blocks depending on conditions.

### Syntax

```python
if condition1:
    # Code executes if condition1 is True

elif condition2:
    # Code executes if condition2 is True

else:
    # Executes if all conditions are False
```

---

# 💻 Example

```python
a = 22

if a > 9:
    print("greater")
else:
    print("lesser")
```

### Output

```
greater
```

---

# 🎯 Practice Question

Write a program that prints **"Yes"** if the user's age is **18 or above**, otherwise print **"No"**.

### Solution

```python
age = int(input("Enter your age: "))

if age >= 18:
    print("Yes")
else:
    print("No")
```

### Sample Output

```
Enter your age: 20
Yes
```

---

# 🔹 Relational Operators

Relational operators compare two values and return either **True** or **False**.

| Operator | Meaning | Example |
|----------|---------|---------|
| `==` | Equal to | `a == b` |
| `!=` | Not equal to | `a != b` |
| `>` | Greater than | `a > b` |
| `<` | Less than | `a < b` |
| `>=` | Greater than or equal to | `a >= b` |
| `<=` | Less than or equal to | `a <= b` |

### Example

```python
x = 10
y = 20

print(x < y)
```

**Output**

```
True
```

---

# 🔹 Logical Operators

Logical operators combine multiple conditions.

## `and`

Returns **True** only if **both conditions are True**.

```python
age = 20
citizen = True

if age >= 18 and citizen:
    print("Eligible to vote")
```

---

## `or`

Returns **True** if **at least one condition is True**.

```python
marks = 85

if marks >= 80 or marks == 100:
    print("Excellent")
```

---

## `not`

Reverses the result.

```python
is_raining = False

if not is_raining:
    print("Let's go outside!")
```

---

# 🔹 The `elif` Statement

`elif` stands for **else if**.

It allows checking multiple conditions one after another.

### Syntax

```python
if condition1:
    # Code

elif condition2:
    # Code

elif condition3:
    # Code

else:
    # Code
```

---

# 💻 Example

```python
marks = 75

if marks >= 90:
    print("Grade A+")

elif marks >= 75:
    print("Grade A")

elif marks >= 60:
    print("Grade B")

else:
    print("Fail")
```

### Output

```
Grade A
```

---

# 📝 Important Notes

- You can use **multiple `elif` statements**.
- The program checks conditions from **top to bottom**.
- Once a condition becomes **True**, the remaining conditions are skipped.
- The **`else` block** executes only if all previous conditions are **False**.



---

# 🎯 Learning Outcomes

After completing this chapter, you will be able to:

- ✅ Understand conditional statements.
- ✅ Use `if`, `elif`, and `else`.
- ✅ Compare values using relational operators.
- ✅ Combine conditions using logical operators.
- ✅ Build simple decision-making programs.

---
Author

Arjun Kumar Giri

Computer Engineering Student | Embedded Systems & IoT Enthusiast

GitHub: https://github.com/arjunkumargiri07


---

### ⭐ If you found this chapter helpful, consider giving the repository a star!
