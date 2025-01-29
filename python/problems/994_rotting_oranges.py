import heapq


def flatten(xss):
    def go(xss, acc):
        match xss:
            case []:
                return acc
            case [xs, *xss]:
                return go(xss, acc + xs)
    return go(xss, [])

class Solution:
    def orangesRotting(self, xss: List[List[int]]) -> int:

        I = len(xss)
        J = len(xss[0])

        def push(xs, prio, i, j):
            for i, j in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= i and i < I and 0 <= j and j < J:
                    heapq.heappush(xs, (prio, (i, j)))

        def bfs(xss):
            def go(q, acc):
                match q:
                    case []:
                        return acc
                    case _:
                        l, (i, j) = heapq.heappop(q)
                        if xss[i][j] == 1:
                            push(q, l + 1, i, j)
                        xss[i][j] = 2
                        return go(q, max(acc, l))

            q = []
            for i in range(I):
                for j in range(J):
                    if xss[i][j] == 2:
                        push(q, 0, i, j)
            return go(q, 0)

        acc = bfs(xss)
        return -1 if 1 in set(flatten(xss)) else acc
        