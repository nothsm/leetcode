from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ps = prices
        max_profit: int = 0
        min_price: int = ps[0]
        for i in range(1, len(ps)):
            max_profit = max(ps[i] - min_price, max_profit)
            min_price = min(ps[i], min_price)
        return max_profit