# Enter your code here. Read input from STDIN. Print output to STDOUT

counter = 0

numbers = input()
output = ""
prev = ""
for i in range(len(numbers)):
    cur = numbers[i]
    if len(numbers) == 1:
        output += f"({1}, {cur})"
    if i == 0:
        counter += 1
        prev = cur
        continue
    if cur == prev:
        counter += 1
    else:
        output += f"({counter}, {prev}) "
        counter = 1
    if i == len(numbers) - 1:
        output += f"({counter}, {cur})"
    prev = cur

print(output)


def betterAnswer(string):
    from itertools import groupby
    print(*[(len(list(c)), int(k)) for k, c in groupby(input())])