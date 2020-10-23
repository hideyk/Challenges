from itertools import product

def printCartesianProduct(i1, i2):
    a = list(product(i1, i2))
    print(*a)


def main():
    input1, input2 = [int(s) for s in input().split()], [int(s) for s in input().split()]
    printCartesianProduct(input1, input2)


if __name__ == "__main__":
    main()