class Solution:
    def lengthOfLongestSubstring(self, xs: str) -> int:
        if not xs:
            return 0
        else:
            l = 0
            r = 1
            cs = {xs[0]: 1}
            acc_len = 1
            acc = 1
            while r < len(xs):
                if not cs.get(xs[r], 0):
                    cs[xs[r]] = cs.get(xs[r], 0) + 1

                    l = l
                    r += 1
                    acc_len += 1
                    acc = max(acc_len, acc)
                else:
                    cs[xs[l]] -= 1

                    l += 1
                    r = r
                    acc_len -= 1
                    acc = max(acc_len, acc)
            return acc
                
        