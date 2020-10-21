import string
d = dict(enumerate(string.ascii_lowercase, 1))


def print_rangoli(size):
    for r in range(size):
        print("-"*(2*(size-r-1)), end="")
        center = size-r
        alpha_list = [d[center]]
        for i in range(r):
            alpha_list.append(d[center+1+i])
            alpha_list.insert(0, d[center+1+i])
        print("-".join(alpha_list), end="")
        print("-"*(2*(size-r-1)))
    for r in range(size-2, -1, -1):
        print("-"*(2*(size-r-1)), end="")
        center = size-r
        alpha_list = [d[center]]
        for i in range(r):
            alpha_list.append(d[center+1+i])
            alpha_list.insert(0, d[center+1+i])
        print("-".join(alpha_list), end="")
        print("-"*(2*(size-r-1)))


print_rangoli(5)