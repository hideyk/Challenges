from typing import List

def numTeams(rating: List[int]) -> int:
        res = 0
        for i in range(1, len(rating) - 1):
            mid = rating[i]
            left = rating[:i]
            right = rating[i+1:]
            leftGreater = sum(x > mid for x in left)
            leftLesser = sum(x < mid for x in left)
            rightGreater = sum(x > mid for x in right)
            rightLesser = sum(x < mid for x in right)
            res += leftGreater * rightLesser
            res += leftLesser * rightGreater
        return res


def main():
    rating = [2,5,3,4,1]
    res = numTeams(rating)
    print(f"Number of teams {res}")

if __name__ == "__main__":
    main()