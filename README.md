# ASCII Art Python

A simple Python command-line tool that converts an image into ASCII art and can print it to the terminal or save it to a text file.

## Features

- Converts JPEG, PNG, and GIF images to ASCII art
- Supports output width configuration
- Supports image rotation with values `0`, `90`, `180`, and `-90`
- Writes ASCII output to a text file or prints it in the terminal
- Includes basic test coverage for success and failure cases

## Requirements

- Python 3
- Pillow
- pytest

## Installation

Install the required dependencies:

```bash
pip install pillow pytest
```

## Usage

Convert an image and print the result:

```bash
python ascii_art.py images/rabbit.jpg --show
```

Write the result to a file:

```bash
python ascii_art.py images/rabbit.jpg --output output.txt --width 60
```

Rotate the output:

```bash
python ascii_art.py images/rabbit.jpg --rotate 90 --show
```

## Project Structure

- `ascii_art.py` — main CLI implementation
- `tests/test_ascii_art.py` — regression tests
- `run.bat` — example Windows batch script
- `requirements/` — project requirements and coding guidance

## Testing

Run the test suite:

```bash
python -m pytest -q
```

## Notes

This project is a lightweight prototype focused on clarity and usability. Future improvements could include better brightness mapping, richer validation, and more advanced formatting options.
