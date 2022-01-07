class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        
        max_profit = 0
        min_price = prices[0]
        for i in range(1, len(prices)):
            profit_forecast = prices[i] - min_price
            max_profit = max(profit_forecast, max_profit)
            min_price = min(min_price, prices[i])
        
        return max_profit
