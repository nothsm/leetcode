import os
import sys

# %%

def lines(s):
    return s.split("\n")

def words(s):
    return s.split(" ")

def rest(s):
    return s[1:]

# %%

def solution_is_primitive(s):
    return isinstance(s, int) and s >= 0

def solution_is_solution(s):
    return isinstance(s, list) and len(s) == 3 and all(c == 0 or c == 1 for c in s)

def solution_is_solutions(ss):
    return isinstance(ss, list) and all(solution_is_solution(s) for s in ss)

def solution_is_implemented(ss):
    return isinstance(ss, list) and len(ss) == 3 and all(isinstance(ss, int))

def solution_read(s):
    return [[int(w) for w in words(line)] for line in s.split("\n")]

def solution_eval(s):
    if solution_is_primitive(s):
        return s
    elif solution_is_solution(s):
        return solution_eval(sum(s) >= 2)
    elif solution_is_solutions(s):
        return solution_eval(sum(map(solution_eval, s)))
    else:
        assert False

test1 = "1 1 0\n1 1 1\n1 0 0"
test2 = "1 0 0\n0 1 1"

def main():
    lines = ''.join(rest(sys.stdin.readlines())).strip()
    print(solution_eval(solution_read(lines)))

if __name__ == '__main__':
    main()
