
'''
doing it recessive would probably be better
'''

def read_phone_number(pn: str) -> dict[str, int]:
    def formatNumber(pn: list[str]) -> dict[str,int]:
        addToVar = lambda edit, num: int(str(edit) + num)
        steps: int = 0
        added: bool = False
        stoppedAt: int = 1
        out: dict[str,int] = {
            "countryCode": 0,
            "areaCode": 0,
            "lineCode": 0
        }
        for num in range(stoppedAt,len(pn)):
            if pn[num].isdigit():
                match steps:
                    case 0:
                        out["countryCode"] = addToVar(out["countryCode"], pn[num])
                    case 1:
                        out["areaCode"] = addToVar(out["areaCode"], pn[num])
                    case 2:
                        out["lineCode"] = addToVar(out["lineCode"], pn[num])
                added = True
            else:
                if added:
                    steps += 1
                    added = False
                stoppedAt = num + 1
        return out
    
    pn = list(pn)
    try:
        if pn[0] == "+" or pn[0] == "(":
            return formatNumber(pn)
    except KeyError as e:
        print(e)
        pass
    return "Not a valid Phone Number"

print(read_phone_number("+123 456 7890") == read_phone_number("(123) 456-7890"))
print(read_phone_number("+519 555 4468") == read_phone_number("(519) 555-4468"))
print(read_phone_number("+345 501 2527") == read_phone_number("(345) 501-2527"))
print(read_phone_number("+345 501 25278") == read_phone_number("(345) 501-25278"))