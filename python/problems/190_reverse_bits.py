from operator import add, sub, mul, neg, lshift, rshift, and_, or_, gt, lt, eq

N_BITS = 32

def dec(x):
    return sub(x, 1)

def sub2(x):
    return sub(x, 2)

def lshift1(x):
    return lshift(x, 1)

def is_pos(x):
    return gt(x, 0)

def is_neg(x):
    return lt(x, 0)

def is_zero(x):
    return eq(x, 0)

def double(x):
    return mul(x, 2)

def bitshift(x, shift):
    if is_pos(shift):
        return lshift(x, shift)
    elif is_neg(shift):
        return rshift(x, neg(shift))
    else:
        return x

class Solution:
    def reverseBits(self, x: int) -> int:
        def go(n, acc, mask, shift):
          if is_zero(n):
            return acc
          else:
            return go(dec(n), 
                      or_(acc, 
                          bitshift(and_(x, mask), 
                                   shift)), 
                      lshift1(mask), 
                      sub2(shift))
        return go(N_BITS, 0, 1, dec(N_BITS))