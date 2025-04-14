# DATA120 Assignment 2 – README

Welcome to your second assignment! This assignment will help you practice key programming concepts like control flow, string manipulation, data structures, functions, and combining everything into a menu-based ordering system. Each part is in **its own Python file**, and directions are **written directly inside the file**. PLEASE make sure to read and follow the comments in each file carefully.

If you have any additional questions, please reach out on Piazza!!!

---

## SUPER IMPORTANT ##
COMMENT YOUR CODE! WRITE DOCSTRINGS FOR YOUR FUNCTIONS! 
COMMENTS AND DOCSTRINGS ARE MANDATORY!!!!!
If you think your code might be confusing, WRITE A COMMENT!
If you've done something complicated, WRITE A COMMENT!
If you've made a variable with an unclear name or purpose, WRITE A COMMENT!
When in doubt, WRITE A COMMENT!

## Files Overview

You’ll be working on the following files:

- `01.py` – Control Flow
- `02.py` – String Manipulation
- `03.py` – Data Structures (for use in Problem 5)
- `04.py` – Functions
- `05.py` – Menu-Based Ordering System (combines previous concepts)

> All instructions are inside each file — read them before you start coding.
> Ask questions on Piazza or attend office hours if you have questions about what you should do! 
> Start early so you have time to ask and we have time to help!

There may also be input files provided for testing — **do not modify them** if they are provided.

---

## ▶️ How to Run Your Code ▶️

Use the terminal to navigate to the folder where your files are saved. To run a file, use the following command:

```bash
python [file_name.py]
or 
python3 [file_name.py]
```

---

## What to Submit?

After you finish coding Problems 1, 2, 3, 4, and 5, you’ll generate a single file that contains the output from those files.

MAKE SURE YOU EXECUTE THESE COMMANDS IN A TERMINAL THAT IS OPEN TO THE SAME FOLDER AS WHERE YOUR
PYTHON FILES ARE!

### Step 1: Generate Your Output File

First, delete any previous `output.txt` to avoid mixing in old output:

- **Mac/Linux:**
  ```bash
  rm output.txt
  ```

- **Windows (Command Prompt):**
  ```bash
  del output.txt
  ```

Then run the following commands in your terminal:

```bash
python3 01.py < inputs/input_01.txt > output.txt
python3 02.py < inputs/input_02.txt >> output.txt
python3 03.py < inputs/input_03.txt >> output.txt
python3 04.py < inputs/input_04.txt >> output.txt
python3 05.py < inputs/input_05.txt >> output.txt
```

> `>` should overwrite .txt files but delete `output.txt` first just to be safe!
> Use `>>` to append outputs to `output.txt` after the first line.

---

### �� Step 2: Submitting ��

- Check that your `output.txt` includes output for Problems 1, 2, 4, and 5
- Upload the following files to Gradescope:
  - `01.py`
  - `02.py`
  - `04.py`
  - `05.py`
  - `output.txt`

---

You're all set — good luck and happy coding! 🎉