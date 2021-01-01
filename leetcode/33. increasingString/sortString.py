def sortString(s: str) -> str:
    res = ""
    while s:
        a = "".join(sorted(set(s)))
        res += a
        for letter in a:
            s = s.replace(letter, "", 1)
        
        if not s:
            break

        b = "".join(sorted(set(s), reverse=True))
        res += b
        for letter in b:
            s = s.replace(letter, "", 1)
    return res

def main():
    s = "aaaabbbbcccc"
    b = sortString(s)
    print(b)

if __name__ == "__main__":
    main()