from itertools import accumulate
from typing import List

def rev(obj):
    return reversed(obj)

def acc(obj, f):
    return accumulate(obj, func=f)

class Solution:
    def trap(self, height: List[int]) -> int:
        hs = height
        lms: List[int] = list(acc(hs, f=max))
        rms: List[int] = list(rev(list(acc(rev(hs), f=max))))
        w: int = 0
        for i in range(len(hs)):
            w += min(lms[i], rms[i]) - hs[i]
        return w