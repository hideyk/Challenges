from typing import List

def countConsistentStrings(allowed: str, words: List[str]) -> int:
    return sum([all([i in allowed for i in x]) for x in words])
    

def main():
    allowed = "ab"
    words = ["ad","bd","aaab","baa","badab"]
    count = countConsistentStrings(allowed, words)
    print(count)

if __name__ == "__main__":
    main()