# BCS2143 / BIT3203 Artificial Intelligence Laboratory

This repository contains the Week 2 Python for Artificial Intelligence laboratory materials for students using Visual Studio Code, local Python and GitHub. Google Colab is not required.

## Laboratory materials

- `notebooks/Wk2a_Python_Rapid_Transition.ipynb`
- `notebooks/Wk2b_Data_Toolkit.ipynb`
- `data/students.csv`
- `data/grades.csv`
- `data/students_messy.csv`
- `src/environment_check.py`
- `requirements.txt`

## Student workflow

Students should create their own repository from this template and clone their own copy into Visual Studio Code.

1. Select **Use this template** on GitHub.
2. Create a new repository under your own GitHub account.
3. Open Visual Studio Code.
4. Press `Ctrl + Shift + P`.
5. Run `Git: Clone`.
6. Paste the address of your own repository.
7. Select a local folder and open the cloned repository.

Full instructions are provided in [STUDENT_SETUP.md](STUDENT_SETUP.md).

## Create the Python environment

Open the repository terminal in Visual Studio Code.

```powershell
py --list
python --version
python -m venv .venv
```

Activate the environment.

```powershell
.\.venv\Scripts\Activate.ps1
```

When PowerShell blocks activation, use Command Prompt.

```cmd
.venv\Scripts\activate.bat
```

Install the required packages.

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Verify the environment.

```powershell
python src\environment_check.py
```

Expected message

```text
AI laboratory environment is ready.
```

## Visual Studio Code configuration

1. Press `Ctrl + Shift + P`.
2. Select `Python: Select Interpreter`.
3. Choose `.venv\Scripts\python.exe`.
4. Open a notebook.
5. Select **Kernel** or **Select Kernel**.
6. Choose the same `.venv` environment.

## Git workflow

After each major exercise

```powershell
git status
git add .
git commit -m "Describe the completed exercise"
git push
```

Do not commit `.venv`, passwords, tokens, API keys or confidential data.
