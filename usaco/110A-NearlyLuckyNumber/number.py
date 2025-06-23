# %%
def last_digit(x):
    return x % 10

def butlast_digit(x):
    return x // 10

def digits(x):
    if x == 0:
        return [0]
    else:
        acc = []
        while x > 0:
            acc.append(last_digit(x))
            x = butlast_digit(x)
        return reversed(acc)

def is_lucky(x):
    return all(d == 4 or d == 7 for d in digits(x))

def is_nearly_lucky(x):
    return is_lucky(sum(is_lucky(d) for d in digits(x)))

def show(x):
    if x:
        return "YES"
    else:
        return "NO"

def read(s):
    return int(s.strip())

def main():
    print(show(is_nearly_lucky(read(input()))))

if __name__ == '__main__':
    main()
