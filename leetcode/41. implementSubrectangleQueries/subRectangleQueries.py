from typing import List

class SubrectangleQueries:
    def __init__(self, rectangle: List[List[int]]):
        self.r = copy.deepcopy(rectangle) # deep copy the input array - credit to @_xavier_
        self.histories = []

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        self.histories.append([row1, col1, row2, col2, newValue])

    def getValue(self, row: int, col: int) -> int:
        for his in reversed(self.histories):
            if his[0] <= row <= his[2] and his[1] <= col <= his[3]:
                return his[4]
        return self.r[row][col]
    
    def __str__(self):
        res = ""
        for row in self.rectangle:
            for obj in row:
                res += f"{obj} "
            res += "\n"
        return res

# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)
 
def main():
    obj = SubrectangleQueries([[1,2,1],[4,3,4],[3,2,1],[1,1,1]])
    print(obj)
    obj.updateSubrectangle(0,0,3,2,5)
    param_2 = obj.getValue(2,1)
    print(obj)
    

if __name__ == "__main__":
    main()