from collections import Counter

def calculateShoeProfit(shoe_sizes, shoe_price_list):
    inventory = Counter(shoe_sizes)
    profit = 0
    for transaction in shoe_price_list:
        if inventory[transaction[0]] >= 1:
            profit += transaction[1]
            inventory[transaction[0]] -= 1
    return profit


def main():
    _ = int(input().strip())
    shoeSizes = [int(x.strip()) for x in input().split()]
    nCustomer = int(input().strip())
    shoePriceList = []
    for i in range(nCustomer):
        size, price = [int(x) for x in input().split()]
        shoePriceList.append([size, price])
    print(calculateShoeProfit(shoeSizes, shoePriceList))


if __name__ == "__main__":
    main()



def betterCalculateProfit():
    numShoes = int(input())
    shoes = Counter(map(int, input().split()))
    numCust = int(input())

    income = 0

    for i in range(numCust):
        size, price = map(int, input().split())
        if shoes[size]:
            income += price
            shoes[size] -= 1

    print(income)