list1 = [2,3,1,5,4]
total = 8

def twoSum(nums, target):
    sortedList = sorted(nums)
    for i in range(len(sortedList)):
        for j in range(i+1, len(sortedList)):
            if sortedList[i] + sortedList[j] == target:
                print([nums.index(sortedList[i]), nums.index(sortedList[j])])


twoSum(list1, total)