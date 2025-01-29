class Solution:
    def pacificAtlantic(self, xss: List[List[int]]) -> List[List[int]]:

        def dfs(xss):
            N, M = len(xss), len(xss[0])
            
            def go(i, j, acc):
                if 0 <= i and i < N and 0 <= j and j < M and (i, j) not in acc:
                    acc.add((i, j))
                    if 0 <= i - 1 and xss[i - 1][j] - xss[i][j] >= 0:
                        go(i - 1, j, acc)
                    if i + 1 < N and xss[i + 1][j] - xss[i][j] >= 0:
                        go(i + 1, j, acc)
                    if 0 <= j - 1 and xss[i][j - 1] - xss[i][j] >= 0:
                        go(i, j - 1, acc)
                    if j + 1 < M and xss[i][j + 1] - xss[i][j] >= 0:
                        go(i, j + 1, acc)

            acc_atl = set()
            acc_pac = set()
        
            for i in range(N):
                go(i, 0, acc_pac)
                go(i, M - 1, acc_atl)

            for j in range(M):
                go(0, j, acc_pac)
                go(N-1, j, acc_atl)

            return acc_atl.intersection(acc_pac)

        return [list(xs) for xs in dfs(xss)]