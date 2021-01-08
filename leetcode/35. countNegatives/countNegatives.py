from typing import List

def countNegatives(grid: List[List[int]]) -> int:
    # 1 brute force approach
    res = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] <= -1:
                res += 1

    # 2 Optimize approach
    res = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] <= -1:
                res += len(grid[y]) - x
                break
    return res

    # 3 Trace the staircase
    m, n = len(grid), len(grid[0])
    r, c, cnt = m - 1, 0, 0
    while r >= 0 and c < n:
        if grid[r][c] <= -1:
            cnt += n - c 
            r -= 1
        else:
            c += 1
    return cnt        

def main():
    grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
#  [  4  3  2 -1]
#  [  3  2  1 -1]
#  [  1  1 -1 -2]
#  [ -1 -1 -2 -3]

if __name__ == "__main__":
    main()