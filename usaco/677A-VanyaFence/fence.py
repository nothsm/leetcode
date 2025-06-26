# %%
import sys

# %%

def read(s):
    # fst, hs = s.split("\n")
    fst, hs = str.split(s, "\n")
    _, h = fst.split()
    return int(h), [int(h) for h in str.split(hs)]

def eval(h, hs):
    def eval1(h, h0):
        return 1 if h0 <= h else 2

    return sum(eval1(h, h0) for h0 in hs)

def main():
    print(eval(*read(sys.stdin.read().strip())))

if __name__ == '__main__':
    main()

# %%

# test1 = "3 7\n4 5 14"
# test2 = "6 1\n1 1 1 1 1 1"
# test3 = "6 5\n7 6 8 9 10 5"

# print(eval(*read(test1)))
# print(eval(*read(test2)))
# print(eval(*read(test3)))
