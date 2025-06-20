# %%

def sum_n(n):
    return (n * (n + 1)) // 2

def cost_banana(k, w):
    return k * sum_n(w)

def main():
    s = input()
    k, n, w = [int(c) for c in s.split()]
    print(max(cost_banana(k, w) - n, 0))

if __name__ == '__main__':
    main()
