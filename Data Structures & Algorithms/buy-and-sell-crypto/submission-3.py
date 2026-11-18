class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price_yet = prices[0]
        max_profit = 0

        for sell in prices:
            max_profit = max(max_profit, sell - min_price_yet)
            min_price_yet = min(sell, min_price_yet)

        return max_profit