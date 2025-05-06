def censor(s: str):
    '''Take a String and Censor words over 4 Characters with stars'''
    s = s.split()
    fin: list[str] = []
    for word in s:
        fin.append(
            word if len(word) < 5 else "*" * len(word)
        )
    return " ".join(fin)

print(censor("The code is fourty"))
print(censor("Two plus three is five"))
print(censor("aaaa aaaaa 1234 12345"))

'''
Expected Output:
censor("The code is fourty")
output = "The code is ******"
censor("Two plus three is five")
output = "Two plus ***** is five"
censor("aaaa aaaaa 1234 12345")
output = "aaaa ***** 1234 *****"
'''