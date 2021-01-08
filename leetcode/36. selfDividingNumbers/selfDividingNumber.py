from typing import List

def selfDividingNumbers(left: int, right: int) -> List[int]:
    res = []
    for i in range(left, right+1):
        if all(i % int(x) == 0 and int(x) for x in str(i)):
            res.append(i)
    return res