def make_adj(xs):
    def go(xs, acc):
        match xs:
            case []:
                return acc
            case [(a, b), *xs]:
                if b not in acc:
                    acc[b] = []
                acc[b].append(a)
                return go(xs, acc)
    return go(xs, {})

class Solution:
    def canFinish(self, n: int, xs: List[List[int]]) -> bool:
        
        adj = make_adj(xs)

        def dfs(x, xs, acc):
            match xs:
                case []:
                    return False
                case [y, *ys] if y in acc:
                    return True
                case [y, *ys]:
                    acc.add(x); has_cycle = dfs(y, adj.get(y, []), acc); acc.remove(x)
                    adj[x].remove(y) # new!
                    return has_cycle or dfs(x, ys, acc)

        def go(xs):
            match xs:
                case []:
                    return False
                case [x, *xs]:
                    return dfs(x, adj.get(x, []), set()) or go(xs)

        return not go(list(range(n)))
