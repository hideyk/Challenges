def freqAlphabets(s: str) -> str:
    res = ""
    while s:
        if len(s) > 2:
            if s[2] == "#":
                res += chr(96+int(s[:2]))
                s = s[3:]
                continue
        res += chr(96+int(s[0]))
        s = s[1:]
    return res

def main():
    s = "10#11#12"
    abc = freqAlphabets(s)
    print(abc)

if __name__ == "__main__":
    main()