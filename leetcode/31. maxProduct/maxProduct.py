from typing import List

def maxProduct(nums: List[int]) -> int:
    a, b = 0, 0
    for num in nums:
        if num > a:
            a, b = num, a
        elif num > b:
            b = num
    return (a - 1) * (b - 1)