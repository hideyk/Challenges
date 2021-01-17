from typing import List
# [ [3, 0, 8, 4], 
#   [2, 4, 5, 7],
#   [9, 2, 6, 3],
#   [0, 3, 1, 0] ]

def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
    res = 0
    n = len(grid)
    for y in range(n):
        for x in range(n):
            res += min(max(grid[y]), max([grid[i][x] for i in range(n)])) - grid[y][x]
    return res

    # Better solution
    # row, col = map(max, grid), map(max, zip(*grid))
    # return sum(min(i, j) for i in row for j in col) - sum(map(sum, grid))