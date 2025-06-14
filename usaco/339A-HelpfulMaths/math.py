# %%
import sys
import os

# %%
def read_sum(s):
    return sorted([int(x) for x in s.split("+")])

def show_sum(xs):
    return "+".join(map(str, xs))

def print_sum(xs):
    print(show_sum(xs))

def main():
    print_sum(read_sum(input()))

if __name__ == '__main__':
    main()


# test1 = "3+2+1"
# test2 = "1+1+3+1+3"

# print(show_sum(read_sum(test1)))
# print(show_sum(read_sum(test2)))
