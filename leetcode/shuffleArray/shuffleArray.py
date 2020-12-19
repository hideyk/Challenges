from typing import List

def shuffle(nums: List[int], n: int) -> List[int]:
    for i in range(n):
        y = n + i
        yi = nums[y]
        del nums[y]
        nums.insert(2*i+1, yi)
    return nums


def bettershuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        for i, j in zip(nums[:n],nums[n:]):
            res += [i,j]
        return res

if __name__ == "__main__":
    abc = [1, 2, 3, 4, 5, 6]
    d = 3
    cba = shuffle(nums=abc, n=d)
    print(cba)
