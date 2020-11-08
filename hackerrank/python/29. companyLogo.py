#!/bin/python3
from collections import Counter

if __name__ == '__main__':
    s = "szrmtbttyyaymadobvwniwmozojggfbtswdiocewnqsjrkimhovimghixqryqgzhgbakpncwupcadwvglmupbexijimonxdowqsjinqzytkooacwkchatuwpsoxwvgrrejkukcvyzbkfnzfvrthmtfvmbppkdebswfpspxnelhqnjlgntqzsprmhcnuomrvuyolvzlni"
    c = Counter(s)
    c = sorted(sorted(c.items(), key=lambda x: x[0]), key=lambda x: x[1], reverse=True)
    topN = 3
    for i in range(topN):
        print(c[i][0], c[i][1])