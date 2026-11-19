# 🛠️ My Toolkit - Reusable Python Function Library

A collection of reusable Python utility functions built to practice core programming concepts such as loops, conditionals, string manipulation, and modular function design.

This project demonstrates how common operations can be implemented manually without relying on certain built-in Python methods, helping strengthen problem-solving and algorithm development skills.

---

## 📌 Project Overview

**My Toolkit** is a small library of reusable Python functions that perform common calculations and data-processing tasks.

The project includes:

- Average calculation
- Maximum and minimum value identification
- Occurrence counting
- Palindrome detection
- Report generation

Several functions intentionally avoid Python convenience methods to demonstrate an understanding of the underlying logic.

---

## 🚀 Functions Included

### 📊 `calculate_average(numbers)`

Calculates the average value of a list of numbers.

**Features:**
- Manually calculates the total using a loop
- Returns `0` when given an empty list
- Does not rely on `sum()`

**Example**

```python
calculate_average([85, 90, 95])
```

**Output**

```text
90.0
```

---

### 🔢 `find_max_and_min(numbers)`

Finds the largest and smallest values in a list without using Python's built-in `max()` or `min()` functions.

**Features:**
- Uses manual comparison logic
- Iterates through the list with a loop
- Returns `(None, None)` for an empty list

**Example**

```python
find_max_and_min([85, 92, 78, 95])
```

**Output**

```text
(95, 78)
```

---

### 🔍 `count_occurrences(items, target)`

Counts how many times a target value appears in a list without using the `.count()` method.

**Example**

```python
count_occurrences([85, 90, 85, 70], 85)
```

**Output**

```text
2
```

---

### 🔄 `is_palindrome(text)`

Determines whether a string reads the same forward and backward.

**Features:**
- Case-insensitive
- Ignores spaces
- Returns a Boolean value

**Example**

```python
is_palindrome("A man a plan a canal Panama")
```

**Output**

```text
True
```

Additional examples:

```python
is_palindrome("racecar")
# True

is_palindrome("hello")
# False

is_palindrome("RaceCar")
# True
```

---

### 📝 `create_report(title, scores)`

Generates a formatted report using information from:

- `calculate_average()`
- `find_max_and_min()`

**Example**

```python
scores = [85, 92, 78, 95, 88, 70, 93]

print(create_report("Class Scores", scores))
```

**Output**

```text
=== Class Scores ===
Average: 85.9
Max: 95
Min: 70
Count: 7
```

---

## 🧠 Concepts Demonstrated

### Python Fundamentals

- Functions
- Parameters and arguments
- Return values
- Lists
- Strings
- Variables

### Control Flow

- `if` statements
- `for` loops
- Conditional comparisons

### Problem Solving

- Manual average calculation
- Custom max/min algorithms
- Counting logic without built-in methods
- String processing

### Software Development Practices

- Modular design
- Reusable functions
- Docstrings
- Edge-case testing
- Main execution guard

---

## 🏗️ Project Structure

```text
my-toolkit/
│
├── my_toolkit.py
└── README.md
```

---

## 🧪 Testing

The project includes both required tests and additional edge-case tests.

### Standard Tests

```python
test_scores = [85, 92, 78, 95, 88, 70, 93]
```

Tests verify:

- Average calculation
- Min/Max detection
- Occurrence counting
- Palindrome detection
- Report generation

### Edge Cases Tested

- Empty list passed to `calculate_average()`
- Empty list passed to `find_max_and_min()`
- Targets appearing multiple times
- Targets appearing zero times
- Mixed-case palindromes
- Palindromes containing spaces
- Single-character strings
- Empty strings

---

## ▶️ Running the Program

From the project directory, run:

```bash
python my_toolkit.py
```

The test suite in the `__main__` block will execute automatically and display results in the terminal.

---

## 🔮 Future Improvements

Potential enhancements include:

- Adding type hints
- Creating automated unit tests with `pytest`
- Packaging the toolkit as an installable module
- Adding additional string utilities
- Adding file-handling helpers
- Adding JSON and CSV processing functions
- Expanding statistical calculations

---

## 👨‍💻 Author

**Grant Eberhardt**

Student software developer focused on Python programming, backend development, problem solving, and building maintainable software solutions.

---

## 📈 Skills Demonstrated

- Python Development
- Algorithm Design
- Function Design
- Data Processing
- String Manipulation
- Control Flow
- Testing and Validation
- Documentation
- Software Development Fundamentals
