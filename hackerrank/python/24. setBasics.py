
def main():
    _ = input()
    a = set(map(int, input().split()))
    _ = input()
    b = set(map(int, input().split()))
    diffa, diffb = a.difference(b), b.difference(a)
    diffa.update(diffb)
    for v in sorted(list(diffa)):
        print(v)

if __name__ == "__main__":
    main()