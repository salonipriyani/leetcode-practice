class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = prices[0]
        for r in range(len(prices)):
            if prices[r] < min_price:
                min_price = prices[r]
            max_profit = max(max_profit, prices[r] - min_price)
        return max_profit

        