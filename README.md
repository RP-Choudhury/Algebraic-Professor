# BIG PROFESSOR: Algebraic Edition
#### Video Demo:  


[Watch on YouTube](https://youtu.be/w9m4ZdEhHi0)
#### Description:
**Big Professor** is an interactive terminal based math game built completely in Python. It takes inspiration from the classic handheld *Little Professor* caclculator. It takes it up a notch by challenging players to solve linear of varied difficulty rather than just artihmetic.

---

## Key Features

- **Object-Oriented Architechture:** Uses a central Professor class which stores the game level, score and even attempts on the visible question.
- **ASCII Terminal Interface:** Uses 'pyfiglet' to directly render a striking banner start screen and answering modules on the terminal.
- **Three Progressive Difficulty Levels:**
    - **Level 1:** Single variable linear equations in the form ($ax + b = c$) using integer values.
    - **Level 2:** Single variable linear equations, again in the form ($ax + b = c$), but this time using floating-point numbers.
    - **Level 3:** Two-Sided Single variable linear eqations in the form ($ax + b = cx + d$) with floating-point numbers
- **Three Attempt Loop:** Provides a three-attempts window per question, and if missed even the third time answer is shown.

---

## File Structure

- `big_professor.py`: The core application file containing the main loop, Professor game class, Terminal formatting methods and the standalone mathematical fuctions for generation of questions and verification of answers.
- `test_big_professor.py`: The Unit tests for the project that verifies the functionality and error checking.
- `requirement.txt`: List of external third-party libraries required to run the application.
- `README.md`: User Guide and Project Documentation
- `CONTRIBUTIONS.md`: Guide to contributions to the Project.
- `LICENSE`: Distributed under the [MIT License](LICENSE).

---

## Setup & Running the Application

1. Install required libraries:
   ```bash
   pip install -r requirements.txt

2. Playing the game:
   ```bash
   python project.py

3. Testing the game:
   ```bash
   pytest test_project.py

## Credits

Thank You, truly if you read till the end. I hope you love the game. Please reach out to me if you want to discuss any new features or any potential bug-fixes.

* **Contributor:** R.P. Choudhury (owner)
* **Github:** [@RP-Choudhury](https://github.com/RP-Choudhury)
* **LinkedIn:** [Rudra Pratap Choudhury](https://www.linkedin.com/in/rudra-pratap-choudhury)
* **License:** Distributed under the [MIT License](LICENSE).




