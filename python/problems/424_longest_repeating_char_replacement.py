class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cs = {}
        max_count = 0
        left, right = 0, 0
        while right < len(s):
            # update cs[s[right]]
            cs[s[right]] = cs.get(s[right], 0) + 1
            max_count = max(max_count, cs[s[right]])
            
            # EXTEND WINDOW CASE
            if (right - left) - max_count < k:
                right += 1
            # SLIDE WINDOW CASE
            else:
                assert (right - left) - max_count == k
                cs[s[left]] = cs[s[left]] - 1
                left += 1
                right += 1
        return right - left