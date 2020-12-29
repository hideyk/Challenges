from typing import List

def diagonalSum(mat: List[List[int]]) -> int:
    size = len(mat)
    sum = 0
    for i in range(size):
        sum += mat[i][i]
        sum += mat[i][size-1-i]
    if size % 2 == 1:
        sum -= mat[size//2][size//2]
    return sum

