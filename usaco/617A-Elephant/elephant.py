STEPS = [1, 2, 3, 4, 5]

def read_elephant(s):
    return int(s)

def eval_elephant(x):
    remaining = x
    s = len(STEPS) - 1
    acc = {}
    while remaining > 0:
        denomination = remaining // STEPS[s]
        remaining = remaining - denomination*STEPS[s]
        acc[STEPS[s]] = denomination
        s -= 1

    while s > 0:
        acc[STEPS[s]] = 0
        s -= 1
    return acc

def denominations_steps(ss):
    return ss.values()

def len_steps(ss):
    return sum(v for v in denominations_steps(ss))


def main():
    print(len_steps(eval_elephant(read_elephant(input()))))

if __name__ == '__main__':
    main()
