# %%
import sys
import os

# %%
def is_lower_str(s):
    return s.islower()

def lower_str(s):
    return s.lower()

def lookup_str(s, i):
    return ord(s[i]) - ord('a')


def compare_char(c1, c2):
    ...

def compare_str(s, t):
    assert is_lower_str(s)
    assert is_lower_str(t)
    assert len(s) == len(t)
    n = len(s)
    i = 0
    ret = 0
    while i < n:
        if lookup_str(s, i) < lookup_str(t, i):
            ret = -1
            break
        elif lookup_str(t, i) < lookup_str(s, i):
            ret = 1
            break
        else:
            i += 1

    return ret


def main():
    print(compare_str(*map(lower_str, sys.stdin.readlines())))

# test1 = ['aaaa', 'aaaA']
# test2 = ['abs', 'Abz']
# test3 = ['abcdefg', 'AbCdEfF']

# print(compare_str(*map(lower_str, test1)))
# print(compare_str(*map(lower_str, test2)))
# print(compare_str(*map(lower_str, test3)))

# %%
if __name__ == '__main__':
    main()
