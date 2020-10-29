_ = int(input())
s = set(map(int, input().split()))
n = int(input())

for i in range(n):
    line = input().split()
    if line[0] == "pop":
        s.pop()
    if line[0] == "remove":
        s.remove(int(line[1]))
    if line[0] == "discard":
        s.discard(int(line[1]))

print(sum(s))