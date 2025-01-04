from functools import partial, reduce
import operator as op

def shape(xss):
    return len(xss), len(xss[0])

def size(xss):
    return reduce(op.mul, shape(xss))

def idxs(axis, i):
    r, c = axis
    return i // c, i % c

def median(lo, hi):
    return ((hi - lo) // 2) + lo

def is_incr(xs):
    for i in range(1, len(xs)):
        if xs[i] <= xs[i-1]:
            return False
    return True

def bound(lo, hi, t, otherwise):
    return (lo if lo < t else otherwise), (hi if hi > t else otherwise)

def search(xss, t):

    idxs_xss = partial(idxs, shape(xss))

    def get(i):
        r, c = idxs_xss(i)
        return xss[r][c]

    def bound(lo, hi, med):
        return lo if t <= get(med) else med, hi if t >= get(med) else med

    lo, hi = 0, size(xss) - 1
    med = median(lo, hi)
    while t not in {get(lo), get(med), get(hi)} and is_incr([lo, med, hi]):
        lo, hi = bound(lo, hi, med)
        med = median(lo, hi)

    return t in {get(i) for i in [lo, med, hi]}

class Solution:
    def searchMatrix(self, xss: List[List[int]], t: int) -> bool:
        return search(xss, t)
