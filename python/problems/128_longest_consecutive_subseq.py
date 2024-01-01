from typing import Dict, List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seqs: Dict[int, int] = dict()
        longest: int = 0

        for n in nums:
            if n not in seqs:
                l: int = seqs.get(n-1, 0)
                r: int= seqs.get(n+1, 0)
                seq_len: int = l + r + 1
                
                seqs[n] = seq_len
                longest = max(seq_len, longest)
                seqs[n-l] = seq_len
                seqs[n+r] = seq_len
        return longest