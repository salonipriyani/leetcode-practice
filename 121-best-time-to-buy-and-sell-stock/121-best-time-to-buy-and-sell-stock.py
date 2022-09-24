class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = windowStart = 0
        min_price = float('inf')
        for windowEnd in range(len(prices)):
            if prices[windowEnd] < min_price:
                min_price = prices[windowEnd]
            elif (prices[windowEnd] - min_price > profit):
                profit = prices[windowEnd] - min_price
                
        return profit