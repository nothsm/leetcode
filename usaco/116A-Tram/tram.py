import sys

# %%

def rest(xs):
    return xs[1:]

def lines(s):
    return str.split(s, "\n")

def words(s):
    return str.split(s, " ")

def read(s):
    return [(int(a), int(b)) for a, b in map(words, rest(lines(s)))]

def eval(expr):
    i = 0
    state = 0
    acc = 0
    while i < len(expr) > 0:
       a, b = expr[i]

       state -= a
       acc = max(state, acc)
       state += b
       acc = max(state, acc)
       i += 1
    return acc

def main():
    print(eval(read(sys.stdin.read().strip())))

if __name__ == '__main__':
    main()

# test1 = "4\n0 3\n2 5\n4 2\n4 0"
# eval(read(test1))
