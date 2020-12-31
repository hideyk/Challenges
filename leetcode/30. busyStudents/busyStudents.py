from typing import List

def busyStudent(startTime: List[int], endTime: List[int], queryTime: int) -> int:
    res = 0
    for i in range(len(startTime)):
        s, e = startTime[i], endTime[i]
        if s <= queryTime and e >= queryTime:
            res += 1
    return res