# %%
def read(s):
    return s.strip()

def len_word(w):
    return len(w)

def upper(s):
    return s.upper()

def lower(s):
    return s.lower()

def uppers(s):
    return ''.join(c for c in s if c.isupper())

def lowers(s):
    return ''.join(c for c in s if c.islower())

def eval(w):
    if len(uppers(w)) > len(lowers(w)):
        return upper(w)
    else:
        return lower(w)

def main():
    print(eval(read(input())))


if __name__ == '__main__':
    main()


# test1 = 'HoUse'
# test2 = 'ViP'
# test3 = 'maTRIx'
