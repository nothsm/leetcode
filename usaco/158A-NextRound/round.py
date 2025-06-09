# %%
import os
import sys

# %%
def round_read(s):
    s_nk, s_ss = s.split("\n")

    s_n, s_k = s_nk.split()
    ss = [int(c) for c in s_ss.split()]
    return ss, int(s_k)

def round_eval(ss, k):
    return sum(s >= ss[k - 1] and s > 0 for s in ss)

def main():
    print(round_eval(*round_read(sys.stdin.read().strip())))

if __name__ == '__main__':
    main()
