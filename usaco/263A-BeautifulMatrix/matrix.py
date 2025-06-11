import sys

# %%

def first(xs):
    return xs[0]

def compose(f, g):
    def h(*a, **kw):
        return f(g(*a, **kw))
    return h

def lines(s):
    return s.split("\n")

def unlines(s):
    return "\n".join(s)

def words(s):
    return s.split(" ")

def unwords(s):
    return " ".join(s)

# %%

def dist_l1(x, y):
    x1, x2 = x
    y1, y2 = y
    return abs(y1 - x1) + abs(y2 - x2)

# %%
def nrows_matrix(xss):
    return len(xss)

def ncols_matrix(xss):
    return len(first(xss))

def middle_matrix(xss):
    return nrows_matrix(xss) // 2, ncols_matrix(xss) // 2

def lookup_matrix(xss, ix):
    i, j = ix
    return xss[i][j]

def one_matrix(xss):
    nrows = nrows_matrix(xss)
    ncols = ncols_matrix(xss)
    return next((i, j) for i in range(nrows) for j in range(ncols) if lookup_matrix(xss, (i, j)) == 1)

def beautiful_matrix(xss):
    return dist_l1(one_matrix(xss), middle_matrix(xss))

def read_matrix(s):
    return [[int(word) for word in line.split(" ")] for line in s.split("\n")]

def show_matrix(xss):
    return unlines(map(compose(unwords,
                               lambda xs: map(str, xs)),
                       xss))

def print_matrix(xss):
    print(show_matrix(xss))

def main():
    print(beautiful_matrix(read_matrix(sys.stdin.read().strip())))

if __name__ == '__main__':
    main()

test1 = [[0, 0, 0, 0, 0],
         [0 ,0, 0, 0, 1],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0]]

test2 = [[0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 1, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0]]
