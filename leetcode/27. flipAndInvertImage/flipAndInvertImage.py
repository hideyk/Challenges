from typing import List
def flipAndInvertImage(A: List[List[int]]) -> List[List[int]]:
    # return [[1 ^ i for i in reversed(row)] for row in A]
    size = len(A)
    for i in range(size):
        for j in range(size//2 + 1):
            back = size-j-1
            if j < back:
                A[i][j], A[i][back] = A[i][back], A[i][j]
                A[i][j] ^= 1
                A[i][back] ^= 1
            elif j == back:
                A[i][j] ^= 1
            else:
                continue
    return A


def main():
    A = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
    B = flipAndInvertImage(A)
    print(B)

if __name__ == "__main__":
    main()