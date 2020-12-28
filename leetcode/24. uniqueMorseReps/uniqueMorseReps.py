from typing import List

def uniqueMorseRepresentations(words: List[str]) -> int:
    morseList = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---",
    "-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."
    ]
    res = set()
    for word in words:
        morse = ""
        for char in word:
            morse += morseList[ord(char)-97]
        res.add(morse)
    return len(res)


def main():
    words = ["gin", "zen", "gig", "msg"]
    uniqueMorses = uniqueMorseRepresentations(words)
    print(uniqueMorses)


if __name__ == "__main__":
    main()