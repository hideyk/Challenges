from typing import List

def oddCells(n: int, m: int, indices: List[List[int]]) -> int:
    odd_count = 0
    rows = [0] * n
    cols = [0] * m

    for i, j in indices:
        rows[i] = rows[i] ^ 1
        cols[j] = cols[j] ^ 1

    for i in range(n):
        for j in range(m):
            if(rows[i] ^ cols[j] == 1): odd_count += 1

    return odd_count


def main():
    n = 2
    m = 3
    indices = [[0,1],[1,1]]
    oddCells(n, m, indices)


if __name__ == "__main__":
    main()