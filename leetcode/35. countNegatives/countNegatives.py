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
def main():
    grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
#  [  4  3  2 -1]
#  [  3  2  1 -1]
#  [  1  1 -1 -2]
#  [ -1 -1 -2 -3]

if __name__ == "__main__":
    main()