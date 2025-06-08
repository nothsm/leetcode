import os

def wexpr_error(s):
    return SyntaxError(f"Expression must be an integral numeral between 1 and 100 (inclusive), got: {s}")

# %%
def wexpr_read(s):
    try:
        expr = int(s)
        if expr < 1 or expr > 100:
            raise wexpr_error(s)
        return expr
    except ValueError as e:
        raise wexpr_error(s)

# %%
def wval_show(x):
    if x:
        return "YES"
    else:
        return "NO"

# %%
def wval_print(x):
    print(wval_show(x))

# %%
def int_is_even(x):
    return x % 2 == 0

# %%

def wexpr_eval(x):
    return any(i + j == x for i in range(1, 101) for j in range(1, 101) if int_is_even(i) and int_is_even(j))


# %%
def wrepl_step():
    wval_print(wexpr_eval(wexpr_read(input("🍉> "))))

def wrepl():
    while True:
        try:
            wrepl_step()
        except (ValueError, SyntaxError) as e:
            print(f"Error: {e}")
            continue

# %%

def test_read(lines):
    return [l.split() for l in lines.strip().split("\n")]

def test_eval(ts, verbose=False):
    passes = 0
    for t in ts:
        arrow = ''
        s, expected = t
        result = wval_show(wexpr_eval(wexpr_read(s)))
        if verbose:
            print(s, '->', result)
        ok = (expected == result)
        passes += ok
        if not ok:
            print('FAIL!!!  Expected', expected)
    print('%s: %d out of %d tests pass.' % ('*'*45, passes, len(ts)))


# %%

def main():
    if "tests.txt" in os.listdir():
        with open("tests.txt", "r") as f:
            test_eval(test_read(f.read()), False)
    wrepl()

if __name__ == '__main__':
    main()
