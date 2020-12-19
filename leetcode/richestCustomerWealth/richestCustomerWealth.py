from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth = sum(accounts[0])
        for i in range(1, len(accounts)):
            curSum = sum(accounts[i])
            if curSum > wealth:
                wealth = curSum
        return wealth