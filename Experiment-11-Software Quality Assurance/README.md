# Experiment 11: Software Quality Assurance

This project applies Software Quality Assurance techniques to a sample login module.

## Project files

- `login.py` — login validation logic
- `main.py` — runs the login program
- `test_login.py` — automated tests
- `docs/Experiment_11_Software_Quality_Assurance_Report.docx` — Experiment Report

## Requirements

- Python 3
- pytest
- coverage
- pylint
- flake8

Install the tools with:

```bash
py -m pip install pytest coverage pylint flake8
```

## Run the program

```bash
py main.py
```

Sample login: username `admin`, password `admin123`.

## Run tests and coverage

```bash
py -m pytest -v
py -m coverage run -m pytest
py -m coverage report -m
```

## Run static analysis

```bash
py -m flake8 login.py
py -m pylint login.py
```
