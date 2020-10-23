import re
from cmath import phase

userInput = input()
result = (int(x) for x in re.findall("[-+]*[0-9]+", userInput))
if userInput[-1] == "j":
    complexNo = complex(*result)
else:
    complexNo = complex(*result[::-1])

print(abs(complexNo))
print(phase(complexNo))