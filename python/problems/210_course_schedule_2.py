def make_adj(xs):
    adj = defaultdict(set)
    for x, p in xs:
        adj[p].add(x)
    return adj

def make_pre(xs):
    pre = defaultdict(list)
    for x, p in xs:
        pre[x].append(p)
    return pre

class Solution:
    def findOrder(self, n: int, xs: List[List[int]]) -> List[int]:
        adj = make_adj(xs)
        ps = make_pre(xs)
        vs = set()
        cs = set()
        acc = []
        def dfs(x):
            assert(len(vs) == len(acc))
            if x in cs:
                return True
            elif x in vs:
                return False
            elif not adj[x]:
                vs.add(x)
                acc.append(x)
                return False
            else:
                vs.add(x)
                acc.append(x)
                cs.add(x)
                for y in list(adj[x]):
                    if all(p in vs for p in ps[y]):
                        if dfs(y): 
                            return True
                        adj[x].remove(y)
                cs.remove(x)
                return False

        for i in range(n):
            if all(p in vs for p in ps[i]):
                if dfs(i): 
                    return []

        return acc if len(acc) == n else []