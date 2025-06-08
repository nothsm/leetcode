import os
import sys
from itertools import islice

# %%
Char = str
Word = list[Char]

# %%

def first(xs):
    return xs[0]

def rest(xs):
    return xs[1:]

def second(xs):
    return xs[1]

def third(xs):
    return xs[2]

def last(xs):
    return xs[-1]

# %%
def is_letter(c):
    return len(c) == 1 and c.isalpha() and c.islower()

# %%
def word_first(w):
    w = first(w)
    assert is_letter(w) and is_word(w)
    return w

def word_last(w):
    w = last(w)
    assert is_letter(w) and is_word(w)
    return w

def word_len(w):
    return len(w)

def word_is_compound(w):
    return all(is_letter(c) for c in w) and 10 < len(w) <= 100

def word_is_primitive(w):
    match w:
        case [fst, n, lst] if isinstance(n, int):
            return is_letter(fst) and 9 <= n <= 98 and is_letter(lst)
        case _:
            return all(is_letter(c) for c in w) and 1 <= len(w) <= 10

def is_word(w):
    return word_is_primitive(w) or word_is_compound(w)

# %%

def word_iter(w):
    return iter(w)

def word_read(s):
    if is_word(list(s)):
        return list(s)
    elif len(s) == 3 and is_word(first(s)) and second(s).isdigit() and int(second(s)) == 9 and is_word(last(s)):
        return [first(s), int(second(s)), last(s)]
    elif len(s) == 4 and is_word(first(s)) and second(s).isdigit() and 10 <= int(second(s) + third(s)) <= 98 and is_word(last(s)):
        return [first(s), int(second(s) + third(s)), last(s)]
    else:
        return None

def word_show(w):
    assert is_word(w)
    return ''.join(map(str, word_iter(w)))

def word_print(w):
    assert is_word(w)
    print(word_show(w))

def word_eval(w):
    assert is_word(w), f"given expression is not a word: {w}"
    if word_is_primitive(w):
        return w
    elif word_is_compound(w):
        return word_eval([word_first(w),
                          word_len(w) - (word_len(word_first(w)) + word_len(word_last(w))),
                          word_last(w)])
    else:
        assert False

# %%

def repl_step():
    try:
        word_print(word_eval(word_read(input("> "))))
    except (TypeError, ValueError, AssertionError):
        print("Error: given word expression but be a string of lowercase Latin letters with length between 1 and 100 (inclusive)")

def repl():
    while True:
        repl_step()

# %%

def test_read(lines):
    return [l.split() for l in lines.strip().split("\n")]

def test_eval(ts, verbose=False):
    passes = 0
    for t in ts:
        arrow = ''
        s, expected = t
        result = word_show(word_eval(word_read(s)))
        if verbose:
            print(s, '->', result)
        ok = (expected == result)
        passes += ok
        if not ok:
            print('FAIL!!!  Expected', expected)
    print('%s: %d out of %d tests pass.' % ('*'*45, passes, len(ts)))

def main():
    if 'tests.txt' in os.listdir():
        with open("tests.txt", "r") as f:
            test_eval(test_read(f.read()), False)
    repl()
    # lines = rest([line.strip() for line in sys.stdin.readlines()])
    # while lines:
    #     word_print(word_eval(first(lines)))
    #     lines = rest(lines)

if __name__ == '__main__':
    main()
