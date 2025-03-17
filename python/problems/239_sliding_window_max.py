from collections import deque

class Solution:
    def maxSlidingWindow(self, xs: List[int], k: int) -> List[int]:
        dq = deque()
        acc = []
        for i, x in enumerate(xs):
            if i < k:
                while dq and i - dq[0][0] >= k:
                    dq.popleft()
                while dq and dq[-1][1] <= x:
                    dq.pop()
                dq.append((i, x))
            else:
                acc.append(dq[0][1])
                while dq and i - dq[0][0] >= k:
                    dq.popleft()
                while dq and dq[-1][1] <= x:
                    dq.pop()
                dq.append((i, x))
        acc.append(dq[0][1])
        return acc