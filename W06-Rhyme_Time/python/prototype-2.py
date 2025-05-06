'''
Task:
Create a function that returns true if two lines rhyme and false otherwise. For the purposes of this
exercise, two lines rhyme if the last word from each s contains the same vowels

Correct Answer =
    Base Examples: True True True False False 
    Extra Examples: True False
'''

import re

def doesRhyme(*args: str) -> bool:

    #* Set Variables
    VOWELS: str = "aeiouy"
    solutions: list[str] = []

    #* Format all inputed strings
        #? @param s = sentence
    for s in args:
        s = s.split()
        s = s[-1].lower()
        s = re.findall(f"[{VOWELS}]", s)
        s = ''.join(s)
        solutions.append(s)

    #* Compare all solutions
    for index in range(len(solutions)):
        try:
            if not solutions[index] == solutions[index + 1]:
                return False
        except:
            pass
    return True


if __name__ == "__main__":
    #? Testing example cases
    print(
        "Base Examples:",
        doesRhyme("Sam I am!", "Green eggs and ham."),
        doesRhyme("Sam I am!", "Green eggs and HAM."),
        doesRhyme("You're built like a seat", "I bet you like to eat"),
        doesRhyme("You are off to the races", "a splendid day."),
        doesRhyme("and frequently do?", "you gotta move."),

        "\nExtra Examples:",
        doesRhyme("Sam I am!", "Green eggs and ham.", "With Sugar and Spam"),
        doesRhyme("Sam I am!", "Green eggs and ham.", "With Sugar and Pig")
    )