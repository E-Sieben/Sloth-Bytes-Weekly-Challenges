def isShuffledWell(shuffeledList: list[int]) -> bool:
    i: int = 0
    while i-2 < len(shuffeledList):
        try:
            if (shuffeledList[i] + 1) == shuffeledList[i+1] and ((shuffeledList[i] + 2) == shuffeledList[i+2]):
                return False
            if (shuffeledList[i] + 1) == shuffeledList[i-1] and ((shuffeledList[i] + 2) == shuffeledList[i-2]):
                return False
        except IndexError:
            pass
        i += 1
    return True

print(isShuffledWell([1, 2, 3, 5, 8, 6, 9, 10, 7, 4]))
output = False
# 1, 2, 3 appear consecutively

print(isShuffledWell([3, 5, 1, 9, 8, 7, 6, 4, 2, 10]))
output = False
# 9, 8, 7, 6 appear consecutively

print(isShuffledWell([1, 5, 3, 8, 10, 2, 7, 6, 4, 9]))
output = True
# No consecutive numbers appear

print(isShuffledWell([1, 3, 5, 7, 9, 2, 4, 6, 8, 10]))
output = True
# No consecutive numbers appear