# %%

def read(s):
    n, k = s.strip().split()
    return int(n), int(k)

def last_digit(x):
    return x % 10

def subtract(n):
    match last_digit(n):
        case 0:
            return n // 10
        case _:
            return n - 1

def eval(n, k):
    while k > 0:
        n = subtract(n)
        k -= 1
    return n

def main():
    print(eval(*read(input())))

if __name__ == '__main__':
    main()

# test1 = "512 4"
# test2 = "1000000000 9"
