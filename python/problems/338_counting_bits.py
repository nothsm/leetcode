def is_zero(x):
    return x == 0

def is_one(x):
    return x == 1

def inc(x):
    return x + 1

def dec(x):
    return x - 1

def is_power_of_2(x):
    return is_zero(x & (dec(x)))

class Solution:
    def countBits(self, n: int) -> List[int]:
        l = 0
        acc = []
        i = 0
        while i < inc(n):
            if is_zero(i):
                acc.append(0)
                i = inc(i)
            elif is_one(i):
                acc.append(1)
                i = inc(i)
            elif is_power_of_2(i):
                acc.append(1)
                l = 1
                i = inc(i)
            else:
                acc.append(inc(acc[l]))
                l = inc(l)
                i = inc(i)
        return acc