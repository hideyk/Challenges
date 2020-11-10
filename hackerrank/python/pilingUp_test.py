import unittest
import collections


popTests = [
    [4, 3, 2, 1, 3, 4],
    [1, 3, 2],
    [3, 3, 3, 3]
]

results = ["Yes", "No", "Yes"]


def pileUpFunc(cubes):
    '''cubes = [4, 3, 2, 1, 3, 4]'''
    d = collections.deque(cubes)
    prev, dir = (d[0], "left") if d[0] >= d[-1] else (d[-1], "right")
    if dir == "left":
        d.popleft()
    else:
        d.pop()
    while d:
        if d[0] >= d[-1]:
            if prev < d[0]:
                return "No"
            else:
                d.popleft()
        else:
            if prev < d[-1]:
                return "No"
            else:
                d.pop()
    return "Yes"


class PileUpTest(unittest.TestCase):
    def testPileUp(self):
        for i in range(len(popTests)):
            with self.subTest(msg=f"{popTests[i]}"):
                self.assertEqual(pileUpFunc(popTests[i]), results[i], msg=f"inner: {popTests[i]}")


if __name__ == "__main__":
    unittest.main()