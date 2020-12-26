def balancedStringSplit(s: str) -> int:
    balance = 0
    result = 0
    for v in s:
        if v == "L":
            balance += 1
        if v == "R":
            balance -= 1
        if balance == 0:
            result += 1
    return result