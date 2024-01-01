from typing import List

# Definition for a pair.
class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value

class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        s: List[List[Pair]] = []
        if not pairs: return s
        
        s.append(list(pairs))
        for i in range(1, len(pairs)):
            next: Pair = pairs[i]
            j: int = i - 1
            while j >= 0 and next.key < pairs[j].key:
                pairs[j+1] = pairs[j]
                j -= 1
            pairs[j+1] = next
            s.append(list(pairs))
        return s