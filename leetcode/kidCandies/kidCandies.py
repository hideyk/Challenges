from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        top = max(candies)
        for i in range(len(candies)):
            candies[i] = candies[i] + extraCandies >= top
        return candies