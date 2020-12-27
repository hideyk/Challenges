import re

def countVowels(s):
    return len([letter for letter in s if letter in 'aeiouAEIOU'])

def halvesAreAlike(s: str) -> bool:
    n = len(s)
    print(n)
    a, b = s[:n//2], s[n//2:]
    return countVowels(a) == countVowels(b)


def main():
    a = "aeiouAEIOU"
    print(halvesAreAlike(a))


if __name__ == "__main__":
    main()