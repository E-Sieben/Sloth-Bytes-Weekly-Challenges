import re

def remove_virus(s: str) -> str:
    """
    Takes String and removes bad files
    """
    badWord: str= r"\b(?!anti|not)(\w*virus|\w*malware)\b"
    badEnding: str = r",? \.\w{1,4},?"
    s = re.sub(badEnding,"",re.sub(badWord, "", s))
    return f"{s} Empty" if s == "PC Files:" else s
    

# ? Test cases
print(remove_virus("PC Files: spotifysetup.exe, virus.exe, dog.jpg"))
print(remove_virus("PC Files: antivirus.exe, cat.pdf, lethalmalware.exe, dangerousvirus.exe "))
print(remove_virus("PC Files: notvirus.exe, funnycat.gif"))
print(remove_virus("PC Files: virus.exe"))