# Chapter 03 - Strings in Python

## 📖 Overview

A **String** is a data type in Python used to store a sequence of characters. Strings are enclosed within quotes and are one of the most commonly used data types in Python programming.

---

## 📝 Creating Strings

Strings can be created in three different ways:

```python
a = 'harry'      # Single quoted string
b = "harry"      # Double quoted string
c = '''harry'''  # Triple quoted string
```

---

## ✂️ String Slicing

String slicing allows you to access a specific portion of a string.

### Example

```python
name = "Harry"
```

| Character | H | a | r | r | y |
| --------- | - | - | - | - | - |
| Index     | 0 | 1 | 2 | 3 | 4 |

### Syntax

```python
string[start:end]
```

Example:

```python
name = "Harry"
print(name[1:4])
```

**Output:**

```python
arr
```

---

## ⏩ Slicing with Skip Value

You can also specify a step value while slicing.

```python
word = "amazing"
print(word[1:6:2])
```

**Output:**

```python
mzn
```

---

## 🔍 Advanced Slicing Techniques

```python
word = "amazing"

print(word[-7:-1])  # amazin
print(word[:7])     # amazing
print(word[0:])     # amazing
```

---

## 🛠️ Common String Functions

### 1. `len()`

Returns the length of the string.

```python
str = "harry"
print(len(str))
```

**Output:**

```python
5
```

---

### 2. `endswith()`

Checks whether a string ends with the specified value.

```python
str = "harry"
print(str.endswith("rry"))
```

**Output:**

```python
True
```

---

### 3. `count()`

Counts the number of occurrences of a character or substring.

```python
str = "harry"
print(str.count("r"))
```

**Output:**

```python
2
```

---

### 4. `capitalize()`

Converts the first character to uppercase.

```python
str = "harry"
print(str.capitalize())
```

**Output:**

```python
Harry
```

---

### 5. `find()`

Returns the index of the first occurrence of a substring.

```python
str = "harry"
print(str.find("rr"))
```

**Output:**

```python
2
```

---

### 6. `replace()`

Replaces all occurrences of a specified substring.

```python
str = "harry"
print(str.replace("r", "l"))
```

**Output:**

```python
hally
```

---

## 🔐 Escape Sequence Characters

Escape sequences are special characters represented using a backslash (`\`).

### Common Escape Sequences

| Escape Sequence | Description  |
| --------------- | ------------ |
| `\n`            | New Line     |
| `\t`            | Tab Space    |
| `\\`            | Backslash    |
| `\'`            | Single Quote |
| `\"`            | Double Quote |

### Example

```python
text = "Hello\nWorld"
print(text)
```

**Output:**

```python
Hello
World
```

---

## 🎯 Key Takeaways

* Strings are sequences of characters enclosed in quotes.
* Python supports single, double, and triple-quoted strings.
* String slicing helps extract specific portions of a string.
* Built-in string functions simplify text manipulation.
* Escape sequence characters add special formatting to strings.

---

### 📚 Learning Series

This README is part of the **Python Programming Handbook – Beginner Friendly Learning Guide**.


