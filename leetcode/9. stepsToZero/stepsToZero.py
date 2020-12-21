def numberOfSteps(num: int) -> int:
    counter = 0
    while num:
        if num % 2 == 0:
            num /= 2
        else:
            num -= 1
        counter += 1
    return counter


# 1 -> 1
# 2 -> 2
# 3 -> 3
# 4 -> 3
# 5 -> 4
# 6 -> 4
# 7 -> 5
# 8 -> 4
# 9 -> 5
# 10 -> 5
# 11 -> 6
# 12 -> 5
# 13 -> 6
# 14 -> 6
# 15 -> 7
# 16 -> 5