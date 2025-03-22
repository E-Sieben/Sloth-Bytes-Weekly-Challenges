def turnCalc(num: int) -> str:
    """Takes in a number and flips it into a word"""
    num: str = str(num)
    num = num[::-1]
    relations: dict[int, str] = {
        "0": "O",
        "1": "I",
        "2": "Z",
        "3": "E",
        "4": "H",
        "5": "S",
        "6": "G",
        "7": "L",
        "8": "B",
        "9": "-", # Genuinly wtf sloth?
    }
    sol: str = ""
    for number in num:
        sol += relations[number]
    return sol

print(turnCalc(707))
output = "LOL"

print(turnCalc(5508))
output = "BOSS"

print(turnCalc(3045))
output = "SHOE"

print(turnCalc("07734"))
output = "HELLO"