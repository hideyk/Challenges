from typing import List

def decompressRLElist(nums: List[int]) -> List[int]:
    output = []
    for i in range(len(nums)//2):
        # 2i for frequency
        # 2i + 1 for value
        freq = nums[2*i]
        val = nums[2*i + 1]
        output += freq * [val]
    return output


def main():
    input = [1, 2, 3, 4]
    output = decompressRLElist(input)
    print(input)
    print(output)

if __name__ == "__main__":
    main()