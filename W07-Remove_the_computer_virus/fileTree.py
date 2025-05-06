def check_dir(path: str, count: int = 0):
    """
    Takes a path and returns the filtered Dir in the path
    """
    import os

    def isVirus(s: str) -> bool:
        """
        Takes a string and returns if it is a virus
        """
        import re
        badWord: str= r"\b(?!anti|not)\w*(virus|malware)\b"
        return bool(re.search(badWord, s, re.IGNORECASE))
    
    dir = os.listdir(path)
    killCount: int = 0
    for file in dir:
        try: # Check if it is a directory and search it recursively
            if not "." in file: 
                directory = check_dir(f"{path}/{file}/", killCount)
                killCount += directory[1]
                print(f"/{file}/{directory[0]}")
        except NotADirectoryError:
            pass

        if isVirus(file): # Check if it is a virus
            dir.remove(file)
            killCount += 1
        
    if not dir: # Check if the directory is empty
        return [["Empty"], killCount]
    
    return dir, killCount

print(f"Removed {check_dir(path='./Solutions/playground/')[1]} Viruses")