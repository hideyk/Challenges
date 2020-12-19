list1 = [2,7,11,15]
total = 9
from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    sortedList = sorted(nums)
    for i in range(len(sortedList)):
        for j in range(i+1, len(sortedList)):
            if sortedList[i] + sortedList[j] == target:
                print([nums.index(sortedList[i]), nums.index(sortedList[j])])

def twoSums(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        v = target - nums[i]
        if v in nums[i+1:]:
            return [i, nums.index(v, i+1)]
            break

twoSums(list1, total)