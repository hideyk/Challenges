from typing import List

def minTimeToVisitAllPoints(points: List[List[int]]) -> int:
    minTime = 0
    for i in range(len(points) - 1):
        a = points[i]
        b = points[i+1]
        while a != b:
            xgreater = a[0] > b[0]
            ygreater = a[1] > b[1]
            xsmaller = a[0] < b[0]
            ysmaller = a[1] < b[1]
            if a[0] == b[0]:
                if ysmaller:
                    a[1] += 1
                else:
                    a[1] -= 1
                minTime += 1
                continue
            if a[1] == b[1]:
                if xsmaller:
                    a[0] += 1
                else:
                    a[0] -= 1
                minTime += 1
                continue
            if xgreater and ygreater:
                a[0] -= 1
                a[1] -= 1
            elif xgreater and ysmaller:
                a[0] -= 1
                a[1] += 1
            elif xsmaller and ygreater:
                a[0] += 1
                a[1] -= 1
            else:
                a[0] += 1
                a[1] += 1
            minTime += 1
    return minTime

def minTimeToVisitAllPoints2(points: List[List[int]]) -> int:
    minTime = 0
    for i in range(1, len(points)):
        prev, cur = points[i-1 : i+1]
        minTime += max([abs(prev[0] - cur[0]), abs(prev[1] - cur[1])])
    return minTime

points = [[1,1],[3,4],[-1,0]]
minTime = minTimeToVisitAllPoints2(points)
print(minTime)