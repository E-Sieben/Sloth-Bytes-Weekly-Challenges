def isLongPressed(original: str, typed: str) -> bool:
    # Init
    mini: str = ""
    i, j = 0, 0

    # Business Logic
    while i < len(typed):
        try:
            if typed[i] == original[j]:
                mini += typed[i]
                j += 1
        except IndexError:
            return False
        i += 1
    
    # Eval
    return True if mini == original else False


#function: isLongPressed(original, typed)
print(isLongPressed("alex", "aaleex"))
#output = true

print(isLongPressed("saeed", "ssaaedd"))
#original contains 2 E's, but the typed only has 1. Not a sticky key issue.
#output = false

print(isLongPressed("leelee", "lleeelee"))
#output = true

print(isLongPressed("Tokyo", "TTokkyoh"))
#An h was typed, not a sticky key problem, just skill issues.
#output = false

print(isLongPressed("laiden", "laiden"))
#output = true