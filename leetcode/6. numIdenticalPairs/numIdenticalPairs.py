from typing import List
from collections import Counter
import math

def getBinomialCounts(n: int, c: int) -> int:
    if n == 1:
        return 0
    if n == 2:
        return 1
    n_fac = math.factorial(n)
    c_fac = math.factorial(c)
    n_c_fac = math.factorial(n - c)
    return int(n_fac/(c_fac*n_c_fac))


def numIdenticalPairs(nums: List[int]) -> int:
    c = Counter(nums)
    total = 0
    for _, v in c.items():
        total += getBinomialCounts(v, 2)
    return total

def betterNumIdenticalPairs(nums: List[int]) -> int:
    return sum([k*(k-1)/2 for k in Counter(nums).values()])