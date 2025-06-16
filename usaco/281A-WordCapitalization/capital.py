def first(xs):
    return xs[0]

def rest(xs):
    return xs[1:]

def capitalize_char(c):
    return c.upper()

def capitalize_word(s):
    return capitalize_char(first(s)) + rest(s)

def main():
    print(capitalize_word(input()))

if __name__ == '__main__':
    main()
