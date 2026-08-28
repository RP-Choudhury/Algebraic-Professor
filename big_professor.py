import random
import re
import pyfiglet

class Professor:

    def __init__(self):
        self.score = 0
        self.show_rules()
        self.attempt = 0

    @property
    def level(self):
        return self._level

    @property
    def score(self):
        return self._score

    @level.setter
    def level(self, level):

        if match := re.search(r"^([1-3])$", level):
            self._level = match.group(1)
        else:
            raise ValueError("Invalid level")

    @score.setter
    def score(self, score):

        self._score = score


    def show_rules(self):
        print(
            f"""
            +==============================================================================+
            |                                                                              |
            |{pyfiglet.figlet_format("            BIG PROFESSOR", font="small").rstrip().replace(chr(10), "           |\n            |")}           |
            |                                                                              |
            |                  ---  A L G E B R A I C   E D I T I O N  ---                 |
            +==============================================================================+
            |                                                                              |
            |  [ RULES ]                                                                   |
            |                                                                              |
            |  0. Select one of Three LEVELs (1) (2) (3).                                  |
            |  1. Solve for 'x' in each generated equation.                                |
            |  2. Round your answer to TWO decimal places when necessary.                  |
            |  3. Trailing zeros are not required (e.g., 1.5 is accepted for 1.50).        |
            |  4. Leading zeros are not required (e.g., .21 is accepted for 0.21).         |
            |  5. You have 3 attempts per equation.                                        |
            |  6. Have Fun!                                                                |
            |                                                                              |
            +==============================================================================+

            """
        )


    def increase_score(self):

        self.score += 1

    def end(self):

        print(
            f"""
            +==============================================================================+
            |                            !!! GREAT JOB !!!                                 |
            |                                                                              |
            |                                                                              |
            |                     Your Score on LEVEL : {self.level}  is {self.score}/10 !                       |
            |                                                                              |
            |                                                                              |
            |                                                                              |
            | ---a game made by RP                                                         |
            +==============================================================================+

            """
        )



#intitialising game and global variables

game = Professor()



def main():
    print(
        """
            +==============================================================================+
            |  LEVEL: [   ]                                                                |
            +==============================================================================+
        """
    )
    game.level = input("\033[3A\033[24C").strip()
    print("\033[3B")

    game_start(10)




def equation(level) -> tuple[str, float]:

    """
    generates an algebraic equation based on the level

    :param level: the difficulty of the game
    :type level: str
    :return: A tuple containing (equation_string , correct_answer)
    :rtype: tuple[str, float]

    """

    if level == "1":


        """
        Level 1: standard integer form ax + b = c

        """

        a = random.randint(1, 9)
        b = random.randint(0, 10)
        c = random.randint(0, 10)
        x = round(float((c-b)/a), 2)

        return (f"{a}x + {b} = {c}", x)

    elif level == "2":

        """
        Level 2: harder variant of level 1, with coefficients and terms being floats and negatives being allowed

        """

        a = round(random.uniform(0.1, 9.9), 1)
        b = round(random.uniform(0.0, 10.0), 1)
        c = round(random.uniform(0.0, 10.0), 1)
        x = round((c-b)/a, 2)

        return (f"{a}x + {b} = {c}", x)


    elif level == "3":

        """
        Level 3: ax + b = cx + d

        """

        a = round(random.uniform(0.1,9.9), 1)
        b = round(random.uniform(0.0,10.0), 1)
        c = round(random.uniform(0.1, a - 0.1), 1)
        d = round(random.uniform(0.0,10.0), 1)
        x = round((d-b)/(a-c), 2 )

        return (f"{a}x + {b} = {c}x + d", x)

    else:

        raise ValueError





def answer_checker(user_ans, ans) -> bool:
    """
    provides True or false depending if answer is correct

    :param user_ans: the answer given by the user
    :type user_ans: float
    :param ans: actual answer
    :type ans: float
    :return: A str pointing answer is correct or wrong depending on whether user_ans is equal or not to ans
    :rtype: bool

    """

    if user_ans == ans:
        game.increase_score()
        return True

    else:
        game.attempt += 1
        return False



def game_start(n=2):

    for _ in range(n):
        question, answer = equation(game.level)
        game.attempt = 0
        print(
            F"""
            +==============================================================================+
               QUESTION: {question}
            +==============================================================================+
            """
        )

        while True:

            print(
                """
            +==============================================================================+
            |  ANSWER:                                                                     |
            +==============================================================================+
                """
            )
            user_ans = float(input("\033[3A\033[26C").strip())
            print("\033[3B")
            if answer_checker(user_ans, answer):
                print(
                    """
            +==============================================================================+
                CORRECT! +1 Point
            +==============================================================================+
                """
                )
                break
            elif game.attempt >= 3:
                game.attempt = 0
                print(
                    f"""
            +==============================================================================+
                THE ANSWER OF {question} WAS {answer}.
            +==============================================================================+
                """
                )
                break

            else:
                print(
                    """
            +==============================================================================+
                LETS TRY AGAIN!
            +==============================================================================+
                """
                )
                continue




    game.end()




if __name__ == "__main__":
    main()
