from collections import Counter

def betterCounter():
    from collections import Counter, OrderedDict
    class OrderedCounter(Counter, OrderedDict):
        pass

    d = OrderedCounter(input() for _ in range(int(input())))
    print(len(d))
    print(*d.values())


def main():
    number_of_words = int(input())
    words = []
    for i in range(number_of_words):
        words.append(input())
    word_counter = Counter(words)
    print(len(word_counter))
    for i in word_counter.values():
        print(i, end=" ")


if __name__ == "__main__":
    main()