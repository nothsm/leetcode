import sys

def translate(s):
    return ''.join(reversed(s))

def eval(exp):
    s, t = exp
    if t == translate(s):
        return 'YES'
    else:
        return 'NO'


def read(s):
    return s.strip().split("\n")

def main():
    print(eval(read(sys.stdin.read())))

if __name__ == '__main__':
    main()

# %%
test1 = ['code', 'edoc']
test2 = ['abb', 'aba']
test3 = ['code', 'code']
tests = [test1, test2, test3]

for test in []:
    print(test, '->', eval(test))
