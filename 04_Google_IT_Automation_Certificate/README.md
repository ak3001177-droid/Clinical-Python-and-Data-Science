# Google IT Automation with Python - Professional Certificate Tracker

This directory serves as a comprehensive tracker for my progress through the Google IT Automation with Python Professional Certificate program. It documents my foundational labs, specialized scripts, and graded milestones across all 6 advanced courses.

---

## 🛠️ Global Program Syllabus & Milestone Progress

### 📘 Course 1: Crash Course on Python (In Progress)
* **Focus:** Syntax, automation logic, data structures, and Object-Oriented Programming (OOP).
* **Progress:** - [x] **Module 1:** Hello Python & Automation Basics (Environment setup, CLI basics)
  - [x] **Module 2:** Basic Python Syntax & Conditionals (Variables, Functions, `if/elif/else`)
  - [x] **Module 3:** Loops and Recursion (Loops iteration, `while` and `for` control flow)
  - [x] **Module 4:** Strings, Lists, and Dictionaries and Object-Oriented Programming(Complex Data Structures) # Module 4: Strings, Lists, and Dictionaries

This folder contains my practice files and master logic codes for Module 4 of the Google IT Automation with Python course. This module transitions from basic syntax to complex Data Structures.

## 📊 Iterable Types Comparison (My Cheat Sheet)

| Data Structure | Definition | Mutable? | Iterable? | Example Representation |
| :--- | :--- | :--- | :--- | :--- |
| **List** | Sequential collection of any data type. | Yes (Can add/remove elements) | Yes (By numeric index) | `['a', 'b', 3, 4]` |
| **Tuple** | Sequential collection of any data type. | **No** (Immutable)* | Yes (By numeric index) | `('commander', 'lambda')` |
| **Dictionary** | Stores `key:value` pairs. | Yes (Values and Keys can update) | Yes (Iterates over keys) | `{'a': [42], 'b': [23]}` |
| **Set** | Unordered collection of *unique* elements. | Yes | Yes (No index) | `{'^2', 'mc', 'E'}` |
| **String** | Sequential collection of textual data. | **No** (Immutable) | Yes (Character sequence)| `"call me ishmael"` |

*\*Note: While tuples are immutable, if a tuple contains a mutable object (like a list), that specific list inside the tuple can be modified.*

## 🛠️ Essential Dictionary Methods

Dictionaries are faster than lists because they use index keys instead of searching sequentially.

* `dictionary.items()`: Returns a live view of the keys and values (Used for `for key, value in...`).
* `dictionary.keys()`: Returns only the keys.
* `dictionary.values()`: Returns only the values.
* `dictionary.get(key, default)`: Returns the value for a key, or a default value if the key doesn't exist (prevents errors).
* `dictionary[key].append(value)`: Appends a new value to an existing key, **ONLY IF** that value is a list.
* `dictionary.update(other_dictionary)`: Replaces existing entries and adds new ones from another dictionary.
* `del dictionary[key]`: Removes a value using its key.
* `dictionary.clear()`: Deletes all items from the dictionary.

**Python 3.9+ specific:**
* `dict1 | dict2`: Merge operator. Combines items. If keys clash, the one on the right wins.
* `dict1 |= dict2`: Update operator. Updates the original dictionary in place.

## ⚡ The Power of List Comprehensions
List comprehensions replace 3-4 lines of a `for` loop into a single, efficient line.

1.  **Basic:** `[action for item in list]`
2.  **With Filter:** `[action for item in list if condition]`
3.  **With If-Else:** `[action_if_true if condition else action_if_false for item in list]`
  - [x] **Module 5:** Final Project (Combining all syntax for a real-world automation tool)

---

### 📙 Course 2: Using Python to Interact with the Operating System (Up Next)
* **Core Focus:** Managing files, directories, running system processes, and handling logs using Python standard libraries (`os`, `sys`, `subprocess`, `re`).
* **Status:** ⏳ Pending

---

### 💻 Course 3: Introduction to Git and GitHub
* **Core Focus:** Advanced Version Control, branching, merging, handling code conflicts, and collaborative development pipelines.
* **Status:** ⏳ Pending

---

### 🔍 Course 4: Troubleshooting and Debugging Techniques
* **Core Focus:** Diagnosing system bottlenecks, memory leaks, performance optimization, and resolving silent application crashes.
* **Status:** ⏳ Pending

---

### ☁️ Course 5: Configuration Management and the Cloud
* **Core Focus:** Deploying automation at scale, managing system configurations using Puppet, and maintaining virtualized cloud infrastructure.
* **Status:** ⏳ Pending

---

### 🚀 Course 6: Automating Real-World Tasks with Python
* **Core Focus:** Capstone architectures, interacting with Web APIs, processing unstructured data, generating automated PDFs, and sending email alerts via code.
* **Status:** ⏳ Pending

---

## 📈 Verification & Quality Assurance
All scripts, lab documentation, and quizzes hosted within this directory are verified against industry standard style guides (PEP 8) to ensure enterprise-ready code quality.