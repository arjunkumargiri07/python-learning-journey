# 📘 Python Programming Handbook
## Chapter 07 – Loops in Python

Beginner Friendly Learning Guide

---

## 📖 Overview

Loops are used to execute a block of code repeatedly without writing the same code multiple times.

For example:

- 🔢 Print numbers from **1 to 1000**
- 📋 Display all items in a list
- 🔄 Repeat a task until a condition becomes false

Python provides two primary types of loops:

- **while loop**
- **for loop**

---

# 📚 Topics Covered

- While Loop
- For Loop
- range() Function
- For Loop with Else
- Break Statement
- Continue Statement
- Pass Statement

---

# 🔹 While Loop

A **while loop** repeatedly executes a block of code as long as the given condition is **True**.

### Syntax

```python
while condition:
    # Code to execute
```

---

## 💻 Example

```python
i = 0

while i < 5:
    print("Harry")
    i = i + 1
```

### Output

```
Harry
Harry
Harry
Harry
Harry
```

---

## 💻 Print Numbers from 1 to 50

```python
i = 1

while i <= 50:
    print(i)
    i += 1
```

---

## 💻 Print Elements of a List Using While Loop

```python
fruits = ["Apple", "Banana", "Mango"]

i = 0

while i < len(fruits):
    print(fruits[i])
    i += 1
```

### Output

```
Apple
Banana
Mango
```

---

# ⚠️ Infinite Loop

If the loop condition **never becomes False**, the loop runs forever.

```python
while True:
    print("This loop never ends!")
```

> **Note:** Use infinite loops carefully, or terminate them using a `break` statement.

---

# 🔹 For Loop

A **for loop** is used to iterate through a sequence such as a list, tuple, string, or range.

### Syntax

```python
for item in sequence:
    # Code
```

---

## 💻 Example

```python
numbers = [1, 7, 8]

for item in numbers:
    print(item)
```

### Output

```
1
7
8
```

---

# 🔹 The `range()` Function

The **range()** function generates a sequence of numbers.

### Syntax

```python
range(start, stop, step)
```

- **start** → Starting value (default = 0)
- **stop** → Ending value (not included)
- **step** → Increment value (default = 1)

---

## 💻 Example 1

```python
for i in range(7):
    print(i)
```

### Output

```
0
1
2
3
4
5
6
```

---

## 💻 Example 2

```python
for i in range(2, 11, 2):
    print(i)
```

### Output

```
2
4
6
8
10
```

---

# 🔹 For Loop with Else

The **else** block executes after the loop completes normally (without a `break`).

### Example

```python
numbers = [1, 7, 8]

for item in numbers:
    print(item)
else:
    print("Done")
```

### Output

```
1
7
8
Done
```

---

# 🔹 Break Statement

The **break** statement immediately exits the loop.

### Example

```python
for i in range(10):
    if i == 3:
        break
    print(i)
```

### Output

```
0
1
2
```

---

# 🔹 Continue Statement

The **continue** statement skips the current iteration and moves to the next one.

### Example

```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```

### Output

```
0
1
3
4
```

---

# 🔹 Pass Statement

The **pass** statement does nothing.

It is used as a placeholder when code is required syntactically but no action is needed.

### Example

```python
numbers = [1, 7, 8]

for item in numbers:
    pass

print("Loop completed.")
```

### Output

```
Loop completed.
```

---

# 📝 Important Notes

- A **while loop** runs until its condition becomes **False**.
- A **for loop** is ideal for iterating through sequences.
- Use **range()** to generate number sequences.
- **break** exits the loop immediately.
- **continue** skips only the current iteration.
- **pass** is a placeholder that performs no operation.
- An **else** block runs only if the loop finishes normally.

---

# 📂 Files Included

```
Chapter07/
│── README.md
│── while_loop.py
│── for_loop.py
│── range_function.py
│── for_else.py
│── break_statement.py
│── continue_statement.py
│── pass_statement.py
```

---

# 🎯 Learning Outcomes

After completing this chapter, you will be able to:

- ✅ Understand the purpose of loops.
- ✅ Use `while` loops effectively.
- ✅ Iterate through sequences using `for` loops.
- ✅ Generate number sequences with `range()`.
- ✅ Control loop execution using `break` and `continue`.
- ✅ Use `pass` as a placeholder.
- ✅ Write efficient programs with repetition.

---

## 🚀 Practice Exercises

1. Print numbers from **1 to 100** using a `while` loop.
2. Print the multiplication table of any number using a `for` loop.
3. Find the sum of numbers from **1 to 50**.
4. Print only the even numbers between **1 and 100**.
5. Use a `break` statement to stop a loop when a specific number is found.
6. Use `continue` to skip all odd numbers.
7. Iterate through a string and print each character separately.

---
Author

Arjun Kumar Giri

Computer Engineering Student | Embedded Systems & IoT Enthusiast

GitHub: https://github.com/arjunkumargiri07


---

### ⭐ If you found this chapter helpful, consider giving the repository a star!
