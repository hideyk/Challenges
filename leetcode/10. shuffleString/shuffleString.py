def restoreString(self, s: str, indices: List[int]) -> str:
        length = len(s)
        slist = [""] * length
        for i in range(length):
            slist[indices[i]] = s[i]
        return "".join(slist)