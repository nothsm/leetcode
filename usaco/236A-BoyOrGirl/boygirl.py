# %%
import sys
import os

# %%
def is_odd(x):
    return x % 2 == 1

def is_male_name(s):
    return is_odd(len(set(s)))

def is_female_name(s):
    return not is_male_name(s)

def is_primitive_name(s):
    return isinstance(s, bool)

def eval_name(s):
    if is_primitive_name(s):
        return s
    else:
        return eval_name(is_male_name(s))

def show_name(s):
    if eval_name(s) is True:
        return "IGNORE HIM!"
    else:
        return "CHAT WITH HER!"

def print_name(s):
    print(show_name(s))

# test1 = 'wjmzbmr'
# test2 = 'xiaodao'
# test3 = 'sevenkplus'

# print_name(test3)

def main():
    print_name(input())

if __name__ == '__main__':
    main()
