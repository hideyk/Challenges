from typing import List

class OrderedStream:
    def __init__(self, n: int):
        self.vals = [0] * n
        self.ptr = 0

    def insert(self, id: int, value: str) -> List[str]:
        self.vals[id-1] = value
        result = []
        while self.vals[self.ptr]:
            result.append(self.vals[self.ptr])
            self.ptr += 1
            if self.ptr == len(self.vals):
                break
        return result


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(id,value)

def main():
    obj = OrderedStream(5)
    param_1 = obj.insert(2,"bbbbb")
    param_2 = obj.insert(1,"aaaaa")
    param_3 = obj.insert(3,"ccccc")
    param_4 = obj.insert(5,"eeeee")
    param_5 = obj.insert(4,"ddddd")
    print(param_1, param_2, param_3, param_4, param_5)

if __name__ == "__main__":
    main()