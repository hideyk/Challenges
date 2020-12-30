from typing import List
from collections import defaultdict

def destCity(paths: List[List[str]]) -> str:
    pathd = defaultdict(lambda: 0)
    for path in paths:
        a, b = path
        pathd[a] -= 1
        pathd[b] += 1
    return list(pathd.keys())[list(pathd.values()).index(1)]


def main():
    paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
    destination = destCity(paths)
    print(destination)

if __name__ == "__main__":
    main()
        