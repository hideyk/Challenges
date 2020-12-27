from typing import List

def sumOddLengthSubarrays(arr: List[int]) -> int:
    size = len(arr)
    res = 0
    for i in range(size):
        for s in range(i, size, 2):
            res += sum(arr[i:s+1])
    return res


def main():
    a = [1, 4, 2, 5, 3]
    print(a[1:2])
    res = sumOddLengthSubarrays(a)
    print(res)

if __name__ == "__main__":
    main()