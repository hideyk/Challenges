if __name__ == '__main__':
    n = int(input())
    print(sorted(list(set(map(int, input().split()))))[-2])