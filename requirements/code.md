# Code Guidelines for ASCII Art Python Project

## Python Version
- Use Python 3 for this project.
- Prefer the latest stable Python 3.x version available in the environment.
- Do not target Python 2.

## Project Goal
- Build a Python command-line tool that converts an image into ASCII art.
- Support common image formats such as JPEG, PNG, and GIF.
- Output the result as plain text to a file and optionally to the terminal.

## Suggested Tech Stack
- Python 3
- Pillow for image loading and processing
- argparse for command-line arguments
- pytest for automated tests

## Coding Standards
- Follow PEP 8 style guidelines.
- Use type hints for function signatures where practical.
- Write small, focused functions with clear responsibilities.
- Add docstrings for public functions and modules.
- Use descriptive names for variables and functions.

## Recommended Project Structure
- main.py or ascii_art.py for the main conversion logic
- cli.py for command-line interface handling
- tests/ for unit tests
- requirements.txt for dependencies

## Dependencies
- Install dependencies from the environment or package manager before running the project.
- Pillow is required for image loading and processing.
- pytest is recommended for automated tests.
- Keep dependency usage minimal for the initial prototype.

## Example CLI Usage
```bash
python ascii_art.py input.jpg --output output.txt --width 80
```

## Implementation Notes
- Use pathlib for file path handling.
- Handle missing files, invalid files, and unsupported formats gracefully.
- Keep the initial implementation simple and readable.
- Focus on correctness and usability before adding advanced features.

## Quality Checklist
- Code runs on Python 3
- Input validation is present
- Errors are reported clearly
- Output is readable plain text
- Basic tests cover success and failure cases
