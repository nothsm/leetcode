# %%

def last_digit(x):
    return x % 10

def butlast_digit(x):
    return x // 10

def digits(x):
    acc = []
    v = x
    while v > 0:
        acc.append(last_digit(v))
        v = butlast_digit(v)
    return list(reversed(acc))

def is_distinct(xs):
    return len(xs) == len(set(xs))

def eval(x):
    acc = x + 1
    while not is_distinct(digits(acc)):
        acc += 1
    return acc

def main():
    print(eval(int(input())))

if __name__ == '__main__':
    main()
