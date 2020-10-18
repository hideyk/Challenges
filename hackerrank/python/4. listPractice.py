if __name__ == '__main__':
    N = int(input())
    initial = []
    for i in range(N):
        action, *args = input().split()
        args = [int(x) for x in args]
        if action == "print":
            print(initial)
        elif action == "insert":
            initial.insert(args[0], args[1])
        elif action == "remove":
            initial.remove(args[0])
        elif action == "append":
            initial.append(args[0])
        elif action == "sort":
            initial.sort()
        elif action == "pop":
            initial.pop()
        elif action == "reverse":
            initial.reverse()




# insert i e: Insert integer  at position .
# print: Print the list.
# remove e: Delete the first occurrence of integer .
# append e: Insert integer  at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.