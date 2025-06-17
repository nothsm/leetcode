import sys
from operator import getitem

# %%

def head(xs):
    return xs[0]

def rest(xs):
    return xs[1:]

def pairs(xs, lookup=getitem, len=len):
    return [(lookup(xs, i), lookup(xs, i + 1)) for  i in range(0, len(xs) - 1)]

# %%

def is_eq_stone(s1, s2):
    return s1 == s2

def lookup_stones(ss, i):
    return ss[i]

def len_stones(ss):
    return len(ss)

def pair_stones(ss):
    return pairs(ss, lookup_stones, len_stones)

def sames_stones(ss):
    return [(s1, s2) for (s1, s2) in pair_stones(ss) if is_eq_stone(s1, s2)]

def read_stones(s):
    return s

def show_stones(ss):
    return ss

def print_stones(ss):
    print(show_stones(ss))

def main():
    s = head(rest(sys.stdin.readlines())).strip()
    ss = read_stones(s)
    out = len(sames_stones(ss))
    print(out)

if __name__ == '__main__':
    main()

# test1 = 'RRG'
# test2 = 'RRRRR'
# test3 = 'BRBG'
# test4 = 'RGB'

# len(sames_stones(test3))
