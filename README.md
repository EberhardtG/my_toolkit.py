# 🛠️ My Toolkit - Reusable Python Function Library

A collection of reusable Python utility functions designed to solve common programming tasks including data analysis, string processing, and report generation.

This project focuses on building foundational software engineering skills by recreating common functionality without relying entirely on Python built-in methods.

---

## 📌 Overview

**My Toolkit** is a Python-based collection of helper functions that can be reused across different applications.

The toolkit includes functions for:

- Calculating averages
- Finding minimum and maximum values
- Counting occurrences
- Checking for palindromes
- Generating formatted reports

The goal of this project was to practice writing modular, reusable code while strengthening understanding of loops, conditionals, functions, and data processing.

---

## 🚀 Features

### 📊 Average Calculator

Calculates the average value from a list of numbers.

Example:

```python
calculate_average([85, 90, 95])
```

Output:

```
90.0
```

Features:
- Handles empty lists safely
- Uses manual accumulation logic
- Avoids relying on `sum()`

---

### 🔢 Min / Max Finder

Finds the highest and lowest values in a list without using:

```python
max()
min()
```

Example:

```python
find_max_and_min([85, 92, 78, 95])
```

Output:

```
(95, 78)
```

Implementation:
- Uses a loop to compare values
- Tracks current highest and lowest values
- Returns both results together

---

### 🔍 Occurrence Counter

Counts how many times a value appears in a list without using:

```python
.count()
```

Example:

```python
count_occurrences([85, 90, 85, 70], 85)
```

Output:

```
2
```

---

### 🔄 Palindrome Checker

Checks whether a string reads the same forward and backward.

Example:

```python
is_palindrome("racecar")
```

Output:

```
True
```

Handles:
- Case conversion
- String comparison
- Boolean return values

---

### 📝 Report Generator

Creates a formatted summary report using previously created functions.

Example:

```python
create_report("Class Scores", scores)
```

Output:

```
=== Class Scores ===
Average: 85.7
Max: 95
Min: 70
Count: 7
```

---

## 🧠 Concepts Practiced

This project demonstrates:

### Python Fundamentals
- Functions
- Parameters and return values
- Variables
- Lists
- Strings

### Control Flow
- `if / else`
- `for` loops
- Conditional comparisons

### Problem Solving
- Recreating built-in functionality
- Tracking values through loops
- Building reusable logic

### Code Organization
- Modular functions
- Documentation strings
- Main execution handling

---

## 🏗️ Project Structure

```
my-toolkit/
│
├── toolkit.py
└── README.md
```

---

## ⚙️ How It Works

The program creates independent utility functions that can be called whenever needed.

Example:

```python
scores = [85, 92, 78, 95]

average = calculate_average(scores)
highest, lowest = find_max_and_min(scores)

print(average)
print(highest)
print(lowest)
```

Each function performs one specific task, making the code easier to test, reuse, and maintain.

---

## ▶️ Running the Project

Clone the repository:

```bash
git clone https://github.com/yourusername/my-toolkit.git
```

Navigate into the project:

```bash
cd my-toolkit
```

Run:

```bash
python toolkit.py
```

---

## 🔮 Future Improvements

Possible enhancements:

- Add unit tests with `pytest`
- Convert toolkit into an installable Python package
- Add error handling for invalid data types
- Expand string utilities
- Add file processing utilities
- Add date/time helper functions
- Add JSON and CSV processing functions

---

## 👨‍💻 Author

**Grant Eberhardt**

Software Engineer building practical Python projects focused on reusable code, problem solving, and application development.

---

## 📈 Skills Demonstrated

- Python Development
- Algorithm Fundamentals
- Data Processing
- Functional Programming
- Code Reusability
- Problem Solving
- Software Design Fundamentals
