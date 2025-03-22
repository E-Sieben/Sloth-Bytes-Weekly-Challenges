class wordCalc:
    """A Calculator word converter"""
    def __init__(self):
        self.relations: dict[int, str] = {
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
        self.reverse_relations = {v: k for k, v in self.relations.items()}
    
    def turnCalc(self, num: any) -> str:
        """Takes in a number and flips it into a word"""
        num = str(num).upper()[::-1]
        
        sol: str = ""
        for number in num:
            sol += self.relations[number]
        return sol
    
    def genNumber(self, word: str) -> str:
        """Takes a Word and converts it into a number (as string type)"""
        sol: str = ""
        for letter in word.upper():
            if letter in self.reverse_relations:
                sol += self.reverse_relations[letter]
        sol = sol[::-1]
        if word.upper() == self.turnCalc(sol):
            return sol
        else:
            return f"Invalid Word, nearest solution {sol}"


if __name__ == "__main__":
    WordCalc: wordCalc = wordCalc()
    print(WordCalc.turnCalc(707))
    output = "LOL"
    print(WordCalc.turnCalc(5508))
    output = "BOSS"
    print(WordCalc.turnCalc(3045))
    output = "SHOE"
    print(WordCalc.turnCalc("07734"))
    output = "HELLO"

    print(WordCalc.genNumber("HELLO"))
    print(WordCalc.genNumber("Let it rain"))
    print(WordCalc.genNumber("Your Joke could stand here"))