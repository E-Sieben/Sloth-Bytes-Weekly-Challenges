def spaceMessage(message: str) -> str:
    result = ""
    i = 0
    while i < len(message):
        if message[i] == "[":
            i += 1
            repeat = ""
            while i < len(message) and message[i].isdigit():
                repeat += message[i]
                i += 1
            repeat: int = int(repeat)
            
            to_repeat = ""
            while i < len(message) and message[i] != "]":
                to_repeat += message[i]
                i += 1
            result += to_repeat * repeat

            if i < len(message) and message[i] == "]":
                i += 1
        else:
            result += message[i]
            i += 1
    
    return result





print("\nTests: ")
print(spaceMessage("ABCD"))
output = "ABCD"

print(spaceMessage("AB[3CD]"))
output = "ABCDCDCD"
# "AB" = "AB"
# "[3CD]" = "CDCDCD"
# Combine both = "ABCDCDCD"

print(spaceMessage("IF[2E]LG[5O]D"))
output = "IFEELGOOOOOD"