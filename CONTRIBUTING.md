# Contributing Guidelines

Thank you for your interest in contributing. 

## Workflow

1. **Fork** this repository on GitHub.

2. **Clone** your fork locally:
   ```bash
   git clone https://github.com/RP-Choudhury/Algebraic-Professor.git
   cd Algebriac-Professor

3. Create a virtual environment and install dependencies
- macOS/Linux/WSL: 
  ```bash
  python3 -m venv .venv
  source .venv/bin/activate
  pip install -r requirements.txt

- Windows(Command Prompt):
  ```cmd
  python -m venv .venv
  .venv\Scripts\activate.bat
  pip install -r requirements.txt

- Windows(PowerShell):
  ```powershell
  python -m venv .venv
  .venv\Scripts\Activate.ps1
  pip install -r requirements.txt

4. Create a **new branch** for your feature or bug fix
   ```bash
   git checkout -b feature/your-branch-name-here

5. Write clean code and make sure to test your code

6. Commit your changes using clear, descriptive messages
   ```bash
   git commit -m "feat: add your-feature-desciption-here"
   ```
   Alternatively:
    
   ```bash
   git config --global core.editor "nvim"
   git commit
   ```
   To add your commit message using neovim

7. Push to your branch and open a **Pull Request (PR)** against the `main` branch.

## Code Standards

- Follow **PEP 8** style guidelines.
- Include unit tests for any new logic added.

## What to expect:

This project is single-handedly managed currently by me, and may not entertain **Pull Requests** as much as other projects.



