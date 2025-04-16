def happyYear(startingYear: int) -> int:
    while True:
        startingYear += 1
        if len(set(str(startingYear))) == len(str(startingYear)):
            return startingYear

def badYear(startingYear: int) -> int:
    return startingYear if len(set(str(startingYear))) == len(str(startingYear)) else badYear(startingYear + 1)

print(badYear(2021))