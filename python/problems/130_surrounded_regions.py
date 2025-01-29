class Solution:
    def solve(self, xss: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        N = len(xss)
        M = len(xss[0])

        acc_v = set()
        def go(i, j, acc):
            if (i == 0 or i == N - 1 or j == 0 or j == M - 1 )and xss[i][j] == 'O':
                return False
            elif xss[i][j] == 'X':
                return True
            elif (i, j) in acc_v:
                return True
            elif (i, j) not in acc_v:
                acc_v.add((i, j))
                acc.add((i, j))

                up = go(i - 1, j, acc)
                down = go(i + 1, j, acc)
                left = go(i, j - 1, acc)
                right = go(i, j + 1, acc)
                return up and down and left and right
                
        for i in range(N):
            for j in range(M):
                if xss[i][j] == 'O':
                    acc = set()
                    if go(i, j, acc):
                        for i2, j2 in acc:
                            xss[i2][j2] = 'X'