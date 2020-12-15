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


alpha = string.ascii_lowercase
def better_rangoli(n):
    L = []
    for i in range(n):
        s = "-".join(alpha[i:n])
        L.append((s[::-1]+s[1:]).center(4*n-3, "-"))
    print('\n'.join(L[:0:-1]+L))

better_rangoli(10)