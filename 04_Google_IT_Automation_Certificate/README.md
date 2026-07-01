# Google IT Automation with Python Professional Certificate

This repository contains my practice files, notes, and projects for the Google IT Automation with Python certificate. 

## 🗺️ Certificate Course Structure
This professional certificate consists of 6 courses:
1. Crash Course on Python
2. Using Python to Interact with the Operating System
3. Introduction to Git and GitHub
4. Troubleshooting and Debugging Techniques
5. Configuration Management and the Cloud
6. Automating Real-World Tasks with Python

---

# Course 1: Crash Course on Python (Master Notes)

This section contains my master logic and cheat sheets for the core Python concepts learned in Course 1.

## 📊 Iterable Types Comparison (Data Structures)

| Data Structure | Definition | Mutable? | Iterable? | Example Representation |
| :--- | :--- | :--- | :--- | :--- |
| **List** | Sequential collection of any data type. | Yes (Can add/remove elements) | Yes (By numeric index) | `['a', 'b', 3, 4]` |
| **Tuple** | Sequential collection of any data type. | **No** (Immutable)* | Yes (By numeric index) | `('commander', 'lambda')` |
| **Dictionary** | Stores `key:value` pairs. | Yes (Values and Keys can update) | Yes (Iterates over keys) | `{'a': [42], 'b': [23]}` |
| **Set** | Unordered collection of *unique* elements. | Yes | Yes (No index) | `{'^2', 'mc', 'E'}` |
| **String** | Sequential collection of textual data. | **No** (Immutable) | Yes (Character sequence)| `"call me ishmael"` |

*\*Note: While tuples themselves are immutable, if a tuple contains a mutable object (like a list), that specific list inside the tuple can be modified.*

---

## 🛠️ Essential Dictionary Methods

Dictionaries are faster than lists because they use index keys instead of searching sequentially.

* `dictionary.items()`: Returns a live view of the keys and values (Used for `for key, value in...`).
* `dictionary.keys()`: Returns only the keys.
* `dictionary.values()`: Returns only the values.
* `dictionary.get(key, default)`: Returns the value for a key, or a default value if the key doesn't exist (prevents errors).
* `dictionary.update(other_dictionary)`: Replaces existing entries and adds new ones from another dictionary.
* `dictionary.copy()`: Makes a safe photocopy of the dictionary so the original remains unchanged.
* `del dictionary[key]`: Removes a value using its key.
* `dictionary.clear()`: Deletes all items from the dictionary.

---

## ⚡ The Magic of List Comprehensions

List comprehensions are a powerful and Pythonic way to create new lists from existing sequences in just **one single line** of code. It replaces 3-4 lines of a traditional `for` loop.

### The 3 Golden Rules & Syntax:

**1. Basic Loop (No Conditions)**
* **Rule:** Do something to every item in the sequence.
* **Formula:** `[action  for  item in list]`
* **Example:** Add 2 to every number in a range.
    ```python
    new_list = [n + 2 for n in range(2, 4)] 
    # Output: [4, 5]
    ```

**2. Filtering with 'If' (Condition at the END)**
* **Rule:** If you only want to extract or keep specific items (and ignore the rest), the `if` statement goes at the *end*.
* **Formula:** `[action  for  item in list  if condition]`
* **Example:** Keep only the odd numbers.
    ```python
    odd_nums = [x for x in range(1, 11) if x % 2 != 0]
    ```

**3. Replacing with 'If-Else' (Condition at the BEGINNING)**
* **Rule:** If you want to modify an item based on a condition (Plan A vs Plan B), the entire `if-else` block must go *before* the `for` loop.
* **Formula:** `[action_if_true  if condition  else action_if_false  for  item in list]`
* **Example:** Rename `.hpp` files to `.h`, but leave other files exactly as they are.
    ```python
    old_files = ["program.c", "stdio.hpp", "a.out"]
    
    updated_files = [file.replace(".hpp", ".h") if file.endswith(".hpp") else file for file in old_files]
    # Output: ['program.c', 'stdio.h', 'a.out']
    ```
    ## 🔤 Essential String Methods

Strings are immutable, meaning they cannot be modified directly. These methods return a *new* string.

* `string.upper()` / `string.lower()`: Converts the string to all uppercase or lowercase.
* `string.strip()`: Removes leading and trailing whitespaces (or specific characters).
* `string.count(substring)`: Returns the number of times a substring appears.
* `string.isnumeric()` / `string.isalpha()`: Returns True if the string contains only numbers or only letters.
* `string.replace(old, new)`: Replaces all occurrences of the old substring with the new one.
* `string.split(delimiter)`: Splits a string into a list of strings based on the delimiter (default is space).
* `delimiter.join(list)`: Joins a list of strings into a single string, separated by the delimiter.

---

## 🏗️ Object-Oriented Programming (OOP) Basics

OOP is a way of organizing code by grouping data and the functions that operate on them into "Objects".

* **Class:** The blueprint or template for creating objects. Defined using the `class` keyword.
* **Instance (Object):** A specific, unique occurrence of a class.
* **Attributes:** Variables that belong to an object (its characteristics, like color or weight).
* **Methods:** Functions that belong to a class (its actions or behaviors). 
* **Docstrings:** Brief text inside `""" """` explaining what a class or method does.

### OOP Syntax Example:
```python
class Apple:
    """This class represents an Apple."""
    
    # Constructor method to initialize attributes
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor

    # A method to describe the apple
    def description(self):
        return "This apple is {} and its flavor is {}.".format(self.color, self.flavor)

# Creating an instance (object) of the Apple class
jonagold = Apple("red", "sweet")

# Calling the method
print(jonagold.description())
# Output: This apple is red and its flavor is sweet.

---


# 🚀 COURSE 2: Using Python to Interact with the Operating System

## 📖 Module 1: Getting Your Python On (Completed)
This module focuses on the fundamentals of using Python to interact directly with the local Operating System, managing packages, and understanding how to write scripts that monitor system health.

### 🛠️ Key Modules & Concepts Learned

#### 1. Built-in Modules (Standard Library)
No installation required for these modules; they come pre-packaged with Python.
* **`math`**: Used for advanced mathematical operations (e.g., `math.sqrt()`, `math.pi`).
* **`shutil`**: Used for high-level file operations and system checks. 
  * *Example:* `shutil.disk_usage("/")` to monitor free disk space.

#### 2. External Modules (Third-Party)
Require installation using the Python Package Manager (`pip`).
* **`arrow`**: A smarter, more human-friendly library for creating, manipulating, and formatting dates and times.
  * *Key functions:* `.now()`, `.shift(days=14)`, `.humanize()` (returns readable formats like "in 2 weeks").
* **`Pillow` (Imported as `PIL`)**: The modern Python Imaging Library used for generating and manipulating image files via code.
  * *Key functions:* `Image.new()`, `img.show()`.
* **`psutil`**: A powerful tool for retrieving information on running processes and system utilization (CPU, memory, disks, network, sensors).
  * *Key functions:* `psutil.cpu_percent()`, `psutil.sensors_battery()`.

### 💻 Scripts Created in this Module
1. **`01_os_basics.py`**: Explored date/time manipulation (Arrow), mathematical calculations (Math), and basic image generation (Pillow).
2. **`02_system_health_check.py`**: Built a real-time system dashboard to monitor Disk Space, CPU Usage, and Battery Status using OS-level commands.

### 📦 Important Terminal Commands
**Package Management:**
```bash
pip install arrow
pip install Pillow
pip install psutil