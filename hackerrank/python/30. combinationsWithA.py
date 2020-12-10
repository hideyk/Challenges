from itertools import combinations

def probabilityContainsA(letters, k):
    combos = combinations(letters, k)
    containsA = []
    comboLength = 0
    for i in combos:
        comboLength += 1
        if "a" in i or "A" in i:
            containsA.append(i)
    return f"{len(containsA)/comboLength:.3f}"

    
n = int(input())
letters = input().replace(" ", "")
k = int(input())
prob = probabilityContainsA(letters, k)
print(prob)