# Chapter 04 - Lists and Tuples in Python

## 📖 Overview

Lists and Tuples are built-in data structures in Python used to store multiple values in a single variable.

* **Lists** are ordered, mutable (changeable) collections.
* **Tuples** are ordered, immutable (unchangeable) collections.

---

# 📋 Lists in Python

A **List** is a container used to store multiple values of different data types.

### Example

```python
l1 = [7, 9, "harry"]
```

Lists can contain integers, strings, floats, and even other lists.

---

## 🔍 List Indexing

Like strings, lists use indexing starting from `0`.

```python
l1 = [7, 9, "harry"]

print(l1[0])  # 7
print(l1[1])  # 9
print(l1[2])  # harry
```

### List Slicing

```python
l1 = [7, 9, "harry"]

print(l1[0:2])
```

**Output:**

```python
[7, 9]
```

---

## 🛠️ Common List Methods

Consider the following list:

```python
l1 = [1, 8, 7, 2, 21, 15]
```

### 1. `sort()`

Sorts the list in ascending order.

```python
l1.sort()
print(l1)
```

**Output:**

```python
[1, 2, 7, 8, 15, 21]
```

---

### 2. `reverse()`

Reverses the order of elements.

```python
l1.reverse()
print(l1)
```

---

### 3. `append()`

Adds an element at the end of the list.

```python
l1.append(8)
print(l1)
```

---

### 4. `insert()`

Inserts an element at a specified index.

```python
l1.insert(3, 8)
print(l1)
```

---

### 5. `pop()`

Removes and returns the element at a specified index.

```python
value = l1.pop(2)
print(value)
```

---

### 6. `remove()`

Removes the specified value from the list.

```python
l1.remove(21)
print(l1)
```

---

# 📦 Tuples in Python

A **Tuple** is an immutable data type in Python.

Once created, its values cannot be modified.

---

## Creating Tuples

### Empty Tuple

```python
a = ()
```

### Tuple with One Element

```python
a = (1,)
```

> ⚠️ A comma is required when creating a tuple with a single element.

### Tuple with Multiple Elements

```python
a = (1, 7, 2)
```

---

## 🛠️ Tuple Methods

Consider the following tuple:

```python
a = (1, 7, 2)
```

### 1. `count()`

Returns the number of times a value occurs.

```python
print(a.count(1))
```

**Output:**

```python
1
```

---

### 2. `index()`

Returns the index of the first occurrence of a value.

```python
print(a.index(1))
```

**Output:**

```python
0
```

---

# 🔄 List vs Tuple

| Feature     | List            | Tuple  |
| ----------- | --------------- | ------ |
| Mutable     | ✅ Yes           | ❌ No   |
| Ordered     | ✅ Yes           | ✅ Yes  |
| Indexed     | ✅ Yes           | ✅ Yes  |
| Syntax      | `[ ]`           | `( )`  |
| Performance | Slightly Slower | Faster |

---
🎯 Key Takeaways
Lists are mutable collections used to store multiple values.
List elements can be accessed using indexing and slicing.
Python provides several built-in methods for list manipulation.
Tuples are immutable collections.
Tuples support methods like count() and index().
Use lists when data needs modification and tuples when data should remain constant.

Author

Arjun Kumar Giri

Computer Engineering Student | Embedded Systems & IoT Enthusiast

GitHub: https://github.com/arjunkumargiri07




