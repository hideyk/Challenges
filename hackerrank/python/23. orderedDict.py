# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

def main():
    quantity = int(input())
    od = OrderedDict()
    for i in range(quantity):
        line = input().split()
        item, cost = " ".join(line[:-1]), float(line[-1])
        if item in od.keys():
            od[item] += cost
        else:
            od[item] = cost
    for k, v in od.items():
        print(k, int(v))

if __name__ == "__main__":
    main()