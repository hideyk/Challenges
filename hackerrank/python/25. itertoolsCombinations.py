# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

word, length = input().split()
word = sorted(word)
length = int(length)

for i in range(1, length+1):
    print("\n".join(["".join(x) for x in combinations(word, i)]))