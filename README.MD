# CLI Terminal Speed Typer

A lightweight, interactive Command Line Interface (CLI) speed typing game built with Python. This tool is designed to test your typing speed and accuracy directly in the terminal using an external dictionary file.

## Features

- **External Word Database:** Automatically loads words from a local `words.txt` file, allowing for easy customization of your vocabulary pool (supports thousands of words).
- **Custom Session Length:** Personalize your session by choosing exactly how many words you want to type.
- **Robust Anti-Duplicate System:** Tracks completed words using a history list to ensure no words are repeated during a single session.
- **Fail-Safe Protection:** Automatically scales down the session length if the requested number of words exceeds the database size, preventing infinite loops.
- **Performance Evaluation:** Tracks total session time and count of mistakes, including a special hidden speed achievement for fast typers.

## Requirements

- Python 3.x

## File Structure

Make sure your files are structured like this in your project folder:
```text
├── words.txt       # Your text file with words (one word per line)
└── typer.py        # The main Python script