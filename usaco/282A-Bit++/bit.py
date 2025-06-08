import sys

# %%

def first(xs):
    return xs[0]

def rest(xs):
    return xs[1:]

# %%

def b_is_prim(bs):
    return isinstance(bs, list) and len(bs) == 0

def b_is_compound(bs):
    return bs and isinstance(bs, list) and all(b_is_stmt(b) for b in bs)

def b_is_inc(b):
    return b == 'inc'

def b_is_dec(b):
    return b == 'dec'

def b_is_stmt(b):
    return b_is_inc(b) or b_is_dec(b)

def b_first(b):
    assert b_is_compound(b)
    return first(b)

def b_rest(b):
    assert b_is_compound(b)
    return rest(b)

# %%

def bread(s):
    if isinstance(s, list):
        return [bread(x) for x in s]
    if s == 'X++' or s == '++X':
        return 'inc'
    elif s == 'X--' or s == '--X':
        return 'dec'
    else:
        assert False

def beval(b, x):
    if b_is_prim(b):
        return x
    if b_is_inc(b):
        return x + 1
    elif b_is_dec(b):
        return x - 1
    elif b_is_compound(b):
        return beval(b_first(b), x) + beval(b_rest(b), x)
    else:
        assert False

# %%

def main():
   s = [line.strip() for line in rest(sys.stdin.readlines())]
   print(beval(bread(s), 0))

if __name__ == '__main__':
    main()
