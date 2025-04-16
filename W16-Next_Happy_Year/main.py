def happyYear(startingYear: int) -> int:
    def isYearHappy(year: int) -> bool:
        for number in str(year):
            occurences: int = 0
            for comparingNumber in str(year):
                if number == comparingNumber:
                    occurences += 1
                    if occurences > 1:
                        return False
        return True

    for year in range(startingYear+1, startingYear+99):
        if isYearHappy(year):
            return year

print(happyYear(2021))