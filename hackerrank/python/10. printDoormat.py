# Enter your code here. Read input from STDIN. Print output to STDOUT

def doormat(r, c):
    for i in range(r//2):
        print((".|."*(i*2+1)).center(c, "-"))
    print("WELCOME".center(c, "-"))
    for i in range(r//2-1, -1, -1):
        print((".|."*(i*2+1)).center(c, "-"))


def main():
    rows, columns = [int(s) for s in input().strip().split()]
    doormat(rows, columns)


if __name__ == "__main__":
    main()