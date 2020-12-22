from typing import List

def restoreString(s: str, indices: List[int]) -> str:
        length = len(s)
        slist = [""] * length
        for i in range(length):
            slist[indices[i]] = s[i]
        return "".join(slist)


def main():
    a = restoreString("abc", [1, 2, 0])
    print(a)
    
if __name__ == "__main__":
    main()