from typing import List

def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
    res = []
    d = {}
    for i, v in enumerate(groupSizes):
        if v == 1:
            res.append([i])
        elif v not in d.keys():
            d[v] = [i]
        else:
            d[v].append(i)
            if len(d[v]) == v:
                res.append(d[v])
                del d[v]
    return res