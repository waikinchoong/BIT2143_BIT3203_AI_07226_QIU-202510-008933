# Student Setup Guide

## 1. Create or sign in to GitHub

1. Open GitHub in a browser.
2. Select **Sign up** or **Sign in**.
3. Use your QIU Google Education email where possible.
4. Verify the email address.
5. Use a professional GitHub username.

## 2. Install the required software

Install these applications before the laboratory.

- Git for Windows
- Visual Studio Code
- Python 3.12 or another lecturer-approved Python 3 version

Restart Visual Studio Code after installation.

## 3. Install Visual Studio Code extensions

Open Extensions using `Ctrl + Shift + X` and install

- Python by Microsoft
- Jupyter by Microsoft
- GitHub Pull Requests and Issues by GitHub

## 4. Create your own repository from the template

1. Open the repository link provided by the lecturer.
2. Select **Use this template**.
3. Select **Create a new repository**.
4. Choose your own GitHub account as the owner.
5. Name the repository using the format requested by the lecturer.
6. Select **Private** for assessed work unless instructed otherwise.
7. Select **Create repository**.

## 5. Clone your repository into Visual Studio Code

1. Open Visual Studio Code.
2. Press `Ctrl + Shift + P`.
3. Select `Git: Clone`.
4. Select **Clone from GitHub** or paste your repository HTTPS address.
5. Choose a local parent folder.
6. Open the cloned repository.
7. Select **Yes, I trust the authors** when prompted.

## 6. Open the repository terminal

Use **Terminal > New Terminal** or press `Ctrl + backtick`.

Confirm the connection.

```powershell
git status
git remote -v
```

The remote address should contain your GitHub username.

## 7. Configure your Git identity

Run these commands inside the repository terminal.

```powershell
git config user.name "Your Full Name"
git config user.email "your-qiu-email@qiu.edu.my"
```

Verify the settings.

```powershell
git config user.name
git config user.email
```

## 8. Create the Python virtual environment

Check the installed Python versions.

```powershell
py --list
python --version
```

Create the environment using the available lecturer-approved version.

```powershell
python -m venv .venv
```

When Python 3.12 is installed, this command may also be used.

```powershell
py -3.12 -m venv .venv
```

Activate it in PowerShell.

```powershell
.\.venv\Scripts\Activate.ps1
```

When PowerShell blocks activation, open a Command Prompt terminal and run

```cmd
.venv\Scripts\activate.bat
```

The terminal prompt should begin with `(.venv)`.

## 9. Install the AI packages

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Verify the installation.

```powershell
python src\environment_check.py
```

Expected message

```text
AI laboratory environment is ready.
```

## 10. Select the Python interpreter and notebook kernel

1. Press `Ctrl + Shift + P`.
2. Select `Python: Select Interpreter`.
3. Choose the interpreter inside `.venv`.
4. Open the required `.ipynb` notebook.
5. Select **Select Kernel**.
6. Choose the same `.venv` Python environment.

## 11. Complete and save the laboratory exercise

Open the notebook specified by the lecturer.

- `notebooks/Wk2a_Python_Rapid_Transition.ipynb`
- `notebooks/Wk2b_Data_Toolkit.ipynb`

Run each cell in order. Read error messages carefully and correct any code requested in the exercise.

## 12. Commit and push your work

```powershell
git status
git add .
git commit -m "Complete Week 2 AI laboratory exercise"
git push
```

Open your repository on GitHub and confirm that the new commit and saved notebook are visible.

## Readiness checklist

- GitHub account is active
- Repository belongs to your GitHub account
- Repository is cloned into Visual Studio Code
- `.venv` has been created and activated
- Required packages are installed
- `.venv` is selected as the interpreter and kernel
- Environment check runs successfully
- Notebook cells run in Visual Studio Code
- Work can be committed and pushed to GitHub

Never commit passwords, access tokens, API keys, confidential datasets or the `.venv` folder.
