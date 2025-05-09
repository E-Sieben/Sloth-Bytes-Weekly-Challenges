def noYelling(sentence: str) -> str:
    sentence: list[str] = list(sentence)
    i: int = 0
    while i < 100:
        if sentence[-2] == "?" or sentence[-2] == "!":
            sentence.pop(-1)
        else:
            return "".join(sentence)

print(noYelling("What went wrong?????????"))
output = "What went wrong?"

print(noYelling("Oh my goodness!!!"))
output = "Oh my goodness!"

print(noYelling("I just!!! can!!! not!!! believe!!! it!!!"))
output = "I just!!! can!!! not!!! believe!!! it!"
# Only change repeating punctuation at the end of the sentence.

print(noYelling("Oh my goodness!"))
output = "Oh my goodness!"
# Do not change sentences where there exists only one or zero exclamation marks/question marks.