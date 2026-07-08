# 📘 Chapter 09: File I/O

This chapter introduces **File Input/Output (File I/O)** in Python. File handling allows programs to store data permanently by reading from and writing to files instead of relying on temporary memory.

---

## 📚 Topics Covered

- Introduction to File I/O
- Types of Files
- Opening a File
- Reading Files
- File Opening Modes
- Writing to Files
- `with` Statement

---

## 💡 What is File I/O?

The data stored in **RAM (Random Access Memory)** is temporary and is erased when a program ends.

To store data permanently, Python uses **files**.

A Python program can:

- Read data from files
- Write data to files
- Update existing files
- Append new data
- Delete files (using additional modules)

---

## 📂 Types of Files

Python mainly works with two types of files:

### 1. Text Files

Examples:

- `.txt`
- `.py`
- `.csv`
- `.html`

These files store readable text.

---

### 2. Binary Files

Examples:

- `.jpg`
- `.png`
- `.mp3`
- `.pdf`
- `.dat`

These files store data in binary format and are not human-readable.

---

## 📁 Opening a File

Python uses the built-in `open()` function to open files.

### Syntax

```python
open("filename", "mode")
```

### Example

```python
f = open("this.txt", "r")
```

---

## 📖 Reading a File

### Example

```python
f = open("this.txt", "r")

text = f.read()

print(text)

f.close()
```

---

## 📄 Reading One Line at a Time

Use the `readline()` method.

### Example

```python
f = open("this.txt", "r")

print(f.readline())
print(f.readline())

f.close()
```

---

## 📌 File Opening Modes

| Mode | Description |
|------|-------------|
| `r` | Read a file (default mode) |
| `w` | Write to a file (overwrites existing content) |
| `a` | Append data to the end of a file |
| `+` | Read and write (update mode) |
| `rb` | Read a binary file |
| `rt` | Read a text file |

---

## ✍️ Writing to a File

Use the `write()` method after opening a file in write (`w`) or append (`a`) mode.

### Example

```python
f = open("this.txt", "w")

f.write("This is nice.")

f.close()
```

---

## 🛡️ Using the `with` Statement

The `with` statement automatically closes the file after its block of code finishes executing.

### Example

```python
with open("this.txt", "r") as f:
    text = f.read()

print(text)
```

### Advantages

- Automatically closes the file
- Prevents resource leaks
- Cleaner and safer code
- Recommended Python practice

---

## ✨ Key Takeaways

- Files provide permanent data storage.
- Python supports both text and binary files.
- The `open()` function is used to access files.
- `read()` reads the entire file.
- `readline()` reads one line at a time.
- `write()` writes data into a file.
- The `with` statement automatically manages file closing.

---

## 🎯 Learning Outcome

After completing this chapter, you will be able to:

- Understand the importance of file handling.
- Open files in different modes.
- Read data from text files.
- Write and append data to files.
- Use the `with` statement for safe and efficient file handling.
- Work with both text and binary files.

---

## 👨‍💻 Author

**Arjun Kumar Giri**

First-Year Computer Engineering Student  
Pokhara Engineering College

---

⭐ If you found this chapter helpful, consider giving the repository a star!
