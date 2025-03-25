N_BITS = 32

def dec(x):
    return x - 1

def sub2(x):
    return x - 2

def shl1(x):
    return x << 1

def is_pos(x):
    return x > 0

def is_neg(x):
    return x < 0

def double(x):
    return 2*x

def bitshift(x, shift):
    if is_pos(shift):
        return x << shift
    elif is_neg(shift):
        return x >> -shift
    else:
        return x

class Solution:
    def reverseBits(self, n: int) -> int:
        acc = 0
        mask = 1
        shift = dec(N_BITS)
        for i in range(N_BITS):
            acc |= bitshift(n & mask, shift)
            mask = shl1(mask)
            shift = sub2(shift)
        return acc