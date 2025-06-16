# %%
import sys
import os

# %%
def words(s):
    return s.split()

# %%
def read_state(s):
    s_l, s_b = words(s)
    return int(s_l), int(s_b)

def step_state(state):
    limak, bob = state
    return 3 * limak, 2 * bob

def eval_state(state, t):
    limak, bob = state
    if limak > bob:
        return t
    else:
        return eval_state(step_state((limak, bob)), t + 1)

def main():
    print(eval_state(read_state(input()), 0))

if __name__ == '__main__':
    main()
