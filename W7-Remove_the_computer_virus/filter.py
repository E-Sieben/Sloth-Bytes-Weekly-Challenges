def remove_virus(s: str) -> str:
    """
    Takes String and removes bad files
    """
    s = s.replace("PC Files: ", "")
    def blacklisted(file: str) -> bool:
        Blacklist: list[str] = ["virus", "malware"]
        return not any(word in file and not ("anti" in file or "not" in file) for word in Blacklist)
    s = ", ".join(filter(blacklisted, s.split(", "))) 
    return f"PC Files: {s if s else "Empty"}"

# ? Test cases
print(remove_virus("PC Files: spotifysetup.exe, virus.exe, dog.jpg"))
print(remove_virus("PC Files: antivirus.exe, cat.pdf, lethalmalware.exe, dangerousvirus.exe "))
print(remove_virus("PC Files: notvirus.exe, funnycat.gif"))
print(remove_virus("PC Files: virus.exe"))