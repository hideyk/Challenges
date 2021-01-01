def generateTheString(n: int) -> str:
    res = "a"
    if n == 1:
        return res
    
    if n % 2 == 0:
        res += "b" * (n - 1)
    else:
        res += "b"
        res += "c" * (n -2)

    return res