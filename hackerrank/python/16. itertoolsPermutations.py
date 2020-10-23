from itertools import permutations


def printPermutations(word, length):
    print("\n".join(["".join(x) for x in list(permutations(sorted(word), length))]))

word, length = input().split()
printPermutations(word, int(length))
