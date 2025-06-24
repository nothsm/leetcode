import sys


def last(xs):
    return xs[-1]

def is_anton(g):
    return g == 'A'

def is_danik(g):
    return g == 'D'

def enumerate_games(gs):
    return enumerate(gs)

def antons(gs):
    return [i for i, g in enumerate_games(gs) if is_anton(g)]

def daniks(gs):
    return [i for i, g in enumerate_games(gs) if is_danik(g)]

def eval_games(gs):
    n_anton = len(antons(gs))
    n_danik = len(daniks(gs))

    if n_anton > n_danik:
        return 'Anton'
    elif n_anton == n_danik:
        return 'Friendship'
    elif n_anton < n_danik:
        return 'Danik'

def read_games(s):
    return last(s.strip().split('\n'))

def main():
   s = sys.stdin.read()
   gs = read_games(s)
   print(eval_games(gs))

if __name__ == '__main__':
    main()

# %%

def run_tests(f, tests):
    print(f.__name__)
    print('\n'.join(repr(x) + ' -> ' + repr(f(x)) for x in tests))

tests_g = ['A',
           'D']
tests_gs = ['ADAAAA',
            'DDDAADA',
            'DADADA']
tests_s = ['6\nADAAAA',
           '7\nDDDAADA',
           '5\nDADADA']

# run_tests(is_anton, tests_g)
# run_tests(is_danik, tests_g)
# run_tests(lambda gs: list(enumerate_games(gs)), tests_gs)
# run_tests(antons, tests_gs)
# run_tests(daniks, tests_gs)
# run_tests(eval_games, tests_gs)
# run_tests(read_games, tests_s)
