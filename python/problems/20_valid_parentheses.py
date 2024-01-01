from typing import List

def is_empty(ss: List[str]) -> bool:
        return len(ss) == 0

def is_open(c: str) -> bool:
    return c == "(" or c == "{" or c == "["

def is_matching(s : str) -> bool:
    return s == "()" or s == "{}" or s == "[]"

class Solution:
    def isValid(self, s: str) -> bool:
        ps: List[str] = []
        for c in s:
            if is_open(c):
                ps.append(c)
            elif is_empty(ps) or not is_matching(ps.pop() + c):
                return False
        return is_empty(ps)