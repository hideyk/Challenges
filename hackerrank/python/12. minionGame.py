def count_substring(substring, string):
    count = 0
    for i in range(len(string)):
        if string[i:i+len(substring)] == substring:
            count += 1
    return count


def get_substrings(string):
    unique_substrings = set()
    for i in range(len(string)):
        ss = ""
        for j in range(i, len(string)):
            ss += string[j]
            unique_substrings.add(ss)
    return unique_substrings


def minion_game(string):
    vowels = "AEIOU"
    usedWords = set()
    stuart, kevin = 0, 0
    for i in range(len(string)):
        for j in range(i+1, len(string)+1):
            newWord = string[i:j]
            if newWord in usedWords:
                continue
            usedWords.add(newWord)
            if newWord[0] in vowels:
                kevin += count_substring(newWord, string)
            else:
                stuart += count_substring(newWord, string)
    winner = "Kevin" if kevin > stuart else "Stuart"
    score = kevin if kevin > stuart else stuart
    if kevin == stuart:
        print("Draw")
    else:
        print(f"{winner} {score}")


def minion_game(string):
    vowel =['A','E','I','O','U']
    S=0
    K=0
    for i in range(len(string)):
        if string[i] in vowel:
            K+= len(string)-i
        else:
            S+=len(string)-i
    if S>K:
        print("Stuart"+" "+ "%d" % S)
    elif K>S:
        print("Kevin"+" "+'%d' % K)
    else:
        print("Draw")



def main():
    word = "BANANA"
    minion_game(word)
    uniques = get_substrings(word)
    print(uniques)


if __name__ == "__main__":
    main()