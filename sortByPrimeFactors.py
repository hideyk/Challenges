def get_prime_factors(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n / 2

    i = 3
    while n != 1:
        if n % i == 0:
            factors.append(i)
            n = n / i
        else:
            i += 2

    return factors


def sort_by_prime_factors(numbers):
    prime_factors = [get_prime_factors(x) for x in numbers]
    return [x for _, x in sorted(zip(prime_factors, numbers))]


def main():
    ini = [10, 20, 30, 40]
    print(get_prime_factors(10))
    res = sort_by_prime_factors(ini)
    print(res)

if __name__ == "__main__":
    main()