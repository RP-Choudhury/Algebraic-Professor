# Big Professor

> An interactive, ingenious terminal based math game built completely in Python.

---
## Overview
Hey, I am **RP**. This is Big Professor the TUI (Terminal User Interface) game developed by me as my final assignment for CS50's Introduction to Programming with Python Course. It is simple fast and easy to understand game which takes inspiration from the 70's classic game, [Little Professor](https://en.wikipedia.org/wiki/Little_Professor).

Like [Little Professor](https://en.wikipedia.org/wiki/Little_Professor), Big Professor too comes with mechanics like levels, attempt based auto-answering and final score calculation. Its graphics include ASCII banners for the end and start screens and a continuous unbroken design style is developed. 

Unlike [Little Professor](https://en.wikipedia.org/wiki/Little_Professor), this is to be played with a calculator. 

---

## Visuals

Starting Banner:
<img width="960" height="903" alt="2026-08-28_18-44-15" src="https://github.com/user-attachments/assets/f6fbfce8-cb96-4e9d-9136-c8ae4a28f9ee" />


End Screen:
<img width="839" height="859" alt="image" src="https://github.com/user-attachments/assets/155e9c9c-0f59-4dfc-90d9-200840dd3f98" />


[Watch a gameplay on YouTube](https://youtu.be/w9m4ZdEhHi0):
<img width="720" height="404" alt="2026-08-28_18-07-40" src="https://github.com/user-attachments/assets/99df42eb-f45e-494b-961a-62f5e14b1141" />

___

## Key Features

- **Object-Oriented Architechture:** Uses a central Professor class which stores the game level, score and even attempts on the visible question.
- **Terminal Interface & Graphics:** Uses `pyfiglet` to directly render a striking banner start screen, answering modules on the terminal and the final end screen with score card.
- **Start Menu:** The Start Menu consists of a banner including rules and more information of how to play the game and navigate difficulty levels.
- **Three Progressive Difficulty Levels:**
    - **Level 1:** Single variable linear equations in the form ($ax + b = c$) using integer values.
    - **Level 2:** Single variable linear equations, again in the form ($ax + b = c$), but this time using floating-point numbers.
    - **Level 3:** Two-Sided Single variable linear eqations in the form ($ax + b = cx + d$) with floating-point numbers
- **Three Attempt Loop:** Provides a three-attempts window per question, and if missed even the third time answer is shown.
- **Score System:** Each correct answer rewards a point in your total score, and scores are calculated out of 10 points, for the 10 questions asked respectively. 
- **Game Over:** The Game Over Menu consists of the end screen with the same art style, your total score and credits. 

## Playing the game:

1. Clone the Repository
   ```bash
   git clone https://github.com/RP-Choudhury/Algebraic-Professor.git
   cd Algebraic-Professor

2. Create and Activate a Virtual Environment
- macOS/Linux/WSL: 
  ```bash
  python3 -m venv .vent
  source .venv/bin/activate
  
- Windows(Command Prompt):
  ```cmd
  python -m venv .venv
  .venv\Scripts\activate.bat
  
- Windows(PowerShell):
  ```powershell
  python -m venv .venv
  .venv\Scripts\Activate.ps1

3. Install Dependencies
   ```bash
   pip install -r requirements.txt
   
4. Launch Big Professor
   ```bash
   python3 big_professor.py

5. Enjoy the game with your calculator

## Credits

Thank You, truly if you read till the end. I hope you love the game. Please reach out to me if you want to discuss any new features or any potential bug-fixes.

* **Contributor:** R.P. Choudhury (owner)
* **Github:** [@RP-Choudhury](https://github.com/RP-Choudhury)
* **LinkedIn:** [Rudra Pratap Choudhury](https://www.linkedin.com/in/rudra-pratap-choudhury)
* **License:** Distributed under the [MIT License](LICENSE).




