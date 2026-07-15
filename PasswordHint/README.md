#Password Hint & Verification Utility 🔐

## 📌 Project Overview
This project is a Python security utility designed to capture user passwords securely, generate dynamic cryptographic structural hints, and perform exact-match verification checks. 

---

## ⚙️ Core Technical Features
- **Input Sanitization:** Uses the `.strip()` method to programmatically eliminate accidental leading and trailing whitespaces, preventing authentication failures caused by input padding.
- **Index Traversal & Case Normalization:** Directly targets string boundaries using standard index positions (`[0]` for the first character and `[-1]` for the final character) while forcing a uniform case structure via `.upper()`.
- **String Interpolation:** Utilizes optimized f-strings to securely build and display structural hint diagnostics to the user.
- **Conditional Match Validation:** Implements a single-line structural conditional `if-else` branching logic to handle binary verification states.

---

## 📁 Project Structure
```text
FNB-Academy-Portfolio/
└── Password-Hint-Utility/
    ├── password_hint.py   # Main application script
    └── README.md          # Project documentation (This file)
```

---


## 🖥️ Expected System Execution Profile

### Case 1: Match Verification Success
```text
Enter your password:   securePass123   
Your password starts with S and ends with 3
Re-enter password: securePass123
Correct password!!
```

### Case 2: Match Verification Failure
```text
Enter your password: myPassword
Your password starts with M and ends with D
Re-enter password: wrongPassword
 Incorrect password
```

---

## 🛡️ Blue Team / Secure Coding Notes
* **Data Leakage Risk:** In genuine banking infrastructure, displaying structural hints (like revealing the first and last letters) reduces the absolute mathematical entropy of a password, making it vulnerable to custom dictionary attacks. This script serves as a proof-of-concept for input string indexing rather than a real-world enterprise authentication mechanism.
* **Format Cleansing:** Stripping whitespace (`.strip()`) before evaluating the boundaries ensures that an accidental spacebar hit does not become the leaked "first character," keeping your validation boundaries mathematically consistent.
