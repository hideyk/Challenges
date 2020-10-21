def solve(s):
    a = '%s' % s
    for i, letter in enumerate(s):
        if s[i] == " ":
            a = a[:i+1] + a[i+1].capitalize() + a[i+2:]
            print(a)
        elif i == 0:
            a = a[i].capitalize() + a[1:]
    return a


def main():
    name = "132 456 Wq  m e"
    print(solve(name))


if __name__ == "__main__":
    main()