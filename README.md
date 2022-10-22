# Specialised Python Filter
A very specialised frontend filter tool for Python projects.
# About
## What The Filter Does
It opens a Python file in the current directory and does the following:
- Goes through each line in the Python file
- Searches for the `{` symbol
- If it finds a result, it will replace `print("` with `print(f"` in the current line
- Creates a new Python file based on the changed data
## What the filter is for

If you put `f` before the starting speech mark in `print()`, then you can use formatting or `{}` as a way of adding variables to a print statement. The task of converting your code to work with the `{}` can be a dull and tedious one, with you having to place hundreds of `f` symbols in front of `print()` statements. You could use a find-and-replace, but that would cause ALL `print()` statements to have the `f` parameter, which is unnecessary and ugly. This tool uses logic to determine if it will replace the `print()` statements in your code with an `f` parameter.

It is incredibly specialised but very helpful.

## Why the code looks terrible
This code was bodged together in literally 15 minutes. I spent more time on the documentation than the actual tool. I used `psf/black` to make sure it didn't look completely abysmal. 

## Support
This tool will NOT be getting support. I will ignore issues and will not be maintaining the code.

# Download and Use
## Install
- Get `Python 3.9+`
- Clone this repo [`git clone https://github.com/WinFan3672/specialised-filter`]
- Open `specialised-auto-filter.py`
## Usage
- Enter the path to a Python file
- The tool will run and exit.
- In the same directory as the Python file, a new file will have been added. If the main Python file is called `file.py`, the new one is called `file_filtered.py`. Also, `file.py.bak` is created, which is a backup of the original file.

# Credits
- Developed solely by `WinFan3672` under the `MIT License`
- Formatted using `Black` [`https://github.com/psf/black/`]
