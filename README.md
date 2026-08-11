# Student Data Management System (Lab Activity 2)

#### Author: Rhenie James C. Reyes
##### DISCLAIMER: This file (README) is AI assisted to improve the readability and flow of the file.

This is a Python program that stores and processes a structured student data which includes: ID, Name, Program, and Year Level. All these data can be edited inside the python program as long as it is running. It does not use a database which stores the data even after the program has ended, but rather, an in-memory data structures that terminates after the process. This program stores and process structured student data using strings, tuples, lists, and dictionaries, with full Create, Read, Update, and Delete (CRUD) functionality.

## Folder Structure

```
reyes_rheniejames_labactivity2/
├── student.py      # Main program (source code)
└── README.md        # This file
```

## Requirements

- Python 3.10+ (uses the `match` statement, introduced in 3.10)
- No external/third-party libraries — only the Python standard library
- Works in Anaconda, a plain Python install, WSL/Ubuntu, or a Python virtual
  environment

## How to Run

1. Open a terminal (WSL, Anaconda Prompt, or any terminal with Python 3.10+ on the PATH).
2. Navigate to the project folder:
   ```bash
   cd reyes_rheniejames_labactivity2
   ```
3. Activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate      # Linux/WSL/macOS
   venv\Scripts\activate         # Windows
   ```
4. Run the program:
   ```bash
   python3 main.py
   ```
5. Use the on-screen menu to add, view, edit, or delete students. Choose
   option `5` to exit.
