from typing import List

def countGoodTriplets(arr: List[int], a: int, b: int, c: int) -> int:
    n = len(arr)
    res = 0
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                va, vb, vc = arr[i], arr[j], arr[k]
                if abs(va-vb) <= a and abs(vb-vc) <= b and abs(va-vc) <= c:
                    res += 1
    return res