# Basic Input and Output using String Format 📋

## 📌 Project Overview
This project, `Project.py`, is a Python script developed as part of my progress *Python*.

The application serves as a **Student Info Formatter**. It collects vital user registration metrics, performs data type verification, processes string transformations, and outputs a neatly styled, terminal-based Student Profile Card.

---

## ⚙️ Core Requirements Met
- **Multi-Type Data Collection:** Captures inputs across all four core foundational primitives: String (`str`), Integer (`int`), and Float (`float`).
- **Input Validation & Type Casting:** Implements explicit runtime type-casting via `int()` and `float()`.
- **String Manipulation:** Transforms text outputs dynamically using `.upper()` and `.title()` methods.
- **Arithmetic Processing:** Calculates exact age metrics in months (`age * 12`).
- **Precision Formatting:** Formats floating-point numbers to exactly 2 decimal places using Python's native `round()` utility.
- **Strict Data Type Verification:** Runs explicit validation checks using the `type()` function to output structural classes.

---

## 📁 Directory Structure
```text
FNB-Academy-Portfolio(PYTHON)/
└── Basic-Input&Format/
    ├── Project.py     # Main application script
    └── README.md      # Project documentation (This file)
```



## 🖥️ Expected Output Profile
```text
=== Student Info System ===

Enter your first name: sbusiso
Enter your surname: khumalo
Enter your age: 19
Enter your favourite number: 7.14682

Welcome, sbusiso khumalo!

========================================
             STUDENT PROFILE CARD             
========================================
Name (UPPERCASE): SBUSISO KHUMALO
Name (Title Case): Sbusiso Khumalo
Age in Months:     228 months
Favourite Number:  7.15
========================================
              DATA TYPE VERIFICATION           
========================================
first_name variable type: <class 'str'>
surname variable type:    <class 'str'>
age variable type:        <class 'int'>
fav_number variable type: <class 'float'>
========================================
```
