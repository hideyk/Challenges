import textwrap


def wrap(string, max_width):
    return "\n".join(textwrap.wrap(string, width=max_width))


if __name__ == '__main__':
    s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(wrap(s, 4))
