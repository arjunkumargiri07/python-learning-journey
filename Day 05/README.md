# Chapter 05: Dictionary & Sets in Python

A beginner-friendly guide to understanding **Dictionaries** and **Sets** in Python.

## 📖 Overview

This chapter covers two important Python data structures:

* **Dictionary** – Stores data in key-value pairs.
* **Set** – Stores unique, non-repetitive elements.

These structures are widely used for efficient data storage, retrieval, and manipulation.

---

## 🔹 Dictionary in Python

A **Dictionary** is a collection of key-value pairs.

### Syntax

```python
a = {
    "key": "value",
    "harry": "code",
    "marks": "100",
    "list": [1, 2, 9]
}

print(a["key"])   # Output: value
print(a["list"])  # Output: [1, 2, 9]
```

### Properties of Dictionaries

* Unordered collection
* Mutable (can be modified)
* Indexed using keys
* Duplicate keys are not allowed

### Common Dictionary Methods

```python
a = {
    "name": "harry",
    "from": "india",
    "marks": [92, 98, 96]
}
```

| Method     | Description                                 |
| ---------- | ------------------------------------------- |
| `items()`  | Returns all key-value pairs as tuples       |
| `keys()`   | Returns all dictionary keys                 |
| `values()` | Returns all dictionary values               |
| `update()` | Updates dictionary with new key-value pairs |
| `get()`    | Returns the value of a specified key        |

### Example

```python
student = {
    "name": "Harry",
    "marks": 95
}

student.update({"city": "Delhi"})

print(student.get("name"))
print(student)
```

---

## 🔹 Sets in Python

A **Set** is a collection of unique (non-repetitive) elements.

### Creating a Set

```python
s = set()

s.add(1)
s.add(2)

print(s)
```

### Properties of Sets

* Unordered
* Unindexed
* No duplicate values allowed
* Elements cannot be accessed using indexes

### Example

```python
s = {1, 2, 2, 3, 4}
print(s)
```

Output:

```python
{1, 2, 3, 4}
```

---

## 🔹 Set Operations

```python
s = {1, 8, 2, 3}
```

| Method           | Description                              |
| ---------------- | ---------------------------------------- |
| `len(s)`         | Returns the number of elements           |
| `remove(x)`      | Removes an element                       |
| `pop()`          | Removes and returns an arbitrary element |
| `clear()`        | Removes all elements                     |
| `union()`        | Combines two sets                        |
| `intersection()` | Returns common elements                  |

### Example

```python
s = {1, 8, 2, 3}

print(len(s))
print(s.union({8, 11}))
print(s.intersection({8, 11}))
```

---

## 📌 Quick Comparison

| Dictionary                 | Set                          |
| -------------------------- | ---------------------------- |
| Stores key-value pairs     | Stores unique values         |
| Accessed using keys        | No indexing                  |
| Duplicate keys not allowed | Duplicate values not allowed |
| Mutable                    | Mutable                      |

---

## 🎯 Learning Outcomes

After completing this chapter, you will be able to:

* Create and use dictionaries in Python.
* Access, update, and retrieve dictionary data.
* Create and manipulate sets.
* Perform common set operations such as union and intersection.
* Understand the differences between dictionaries and sets.



