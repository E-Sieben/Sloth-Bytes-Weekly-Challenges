# Idea use a language with static types using a unsinged Integer and use the error when going out of bounds as return
def lemonade(orders: list[int]) -> bool:
    fives: int = 0
    tens: int = 0

    for order in orders:
        match order:
            case 5:
                fives += 1
            case 10:
                tens += 1
                if fives > 0: #! Give back a five dollar note
                    fives -= 1
                else:
                    return False
            case 20:
                if tens > 0 and fives > 0: #! Give back a Ten and a Five dollar note
                    tens -= 1
                    fives -= 1
                elif fives >= 3: #! Give back three five dollar notes
                    fives -= 3
                else:
                    return False
    return True

print(lemonade([5, 5, 5, 10, 20]))
print(lemonade([5, 5, 10, 10, 20]))
print(lemonade([10, 10]))
print(lemonade([5, 5, 10]))

# true, false, false, true