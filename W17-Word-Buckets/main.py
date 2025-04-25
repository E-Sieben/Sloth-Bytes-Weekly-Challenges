def split_into_buckets(sentence: str, size: int) -> list[str]:
    words = sentence.split(" ")
    split_sentences: list[str] = []
    i: int = 0
    while i < len(words):
        if len(words[i]) > size:
            i += 1
            continue
        elif len(words[i]) == size:
            split_sentences.append(words[i])
            i += 1
        else:
            compound: str = words[i]
            j: int = i + 1
            while j < len(words):
                prev_compound: str = compound
                if j < len(words):
                    compound = compound + " " + words[j]
                if len(compound) > size:
                    split_sentences.append(prev_compound)
                    i = j
                    break
                elif len(compound) == size:
                    split_sentences.append(compound)
                    i = j + 1
                    break
                j += 1
            if j == len(words):
                split_sentences.append(compound)
                i = j
    return split_sentences


print(split_into_buckets("she sells sea shells by the sea", 10)) # Success
print(split_into_buckets("the mouse jumped over the cheese", 7)) # Success
print(split_into_buckets("fairy dust coated the air", 20)) # Success
print(split_into_buckets("a b c d e", 2)) # Success

