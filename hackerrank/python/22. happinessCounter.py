def main():
    n, m = map(int, input().split())
    commonArray = list(map(int, input().split()))
    like = set(map(int, input().split()))
    dislike = set(map(int, input().split()))
    print(sum([(i in like) - (i in dislike) for i in commonArray]))


if __name__ == "__main__":
    main()
