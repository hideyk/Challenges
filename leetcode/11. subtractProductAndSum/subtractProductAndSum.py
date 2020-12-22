def subtractProductAndSum(n: int) -> int:
    product = 1
    total = 0
    while n:
        v = n % 10
        total += v
        product *= v
        n = n // 10
    return product - total