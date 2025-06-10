# %%
def domino_read(s):
    s_m, s_n = s.split()
    return int(s_m), int(s_n)

def domino_eval(m, n):
    return (m * n) // 2

def main():
    print(domino_eval(*domino_read(input())))

if __name__ == '__main__':
    main()

"""
eval 2 4 = 4
. . . .
. . . .

eval 3 3 = 4
. . .
. . .
. . .

eval 1 1 = 0
.

eval 1 2 = 1
. .

eval 1 3 = 1
. . .

eval 1 4 = 2
. . . .

eval 1 5 = 2
. . . . .

eval 1 6 = 3
. . . . . .

eval 2 1 = 1
.
.

eval 2 2 = 2
. .
. .

eval 2 3 = 3
. . .
. . .

eval 2 4 = 4
. . . .
. . . .

eval 2 5 = 5
. . . . .
. . . . .

eval 2 6 = 6
. . . . . .
. . . . . .

eval 3 1 = 1
.
.
.

eval 3 2 = 3
. .
. .
. .

eval 3 3 = 4
. . .
. . .
. . .

eval 3 4 = 6
. . . .
. . . .
. . . .

eval 3 5 = 7
. . . . .
. . . . .
. . . . .

eval 3 6 = 9
. . . . . .
. . . . . .
. . . . . .

eval 3 7 = 10
. . . . . . .
. . . . . . .
. . . . . . .

eval 3 8 = 12
. . . . . . . .
. . . . . . . .
. . . . . . . .
"""
