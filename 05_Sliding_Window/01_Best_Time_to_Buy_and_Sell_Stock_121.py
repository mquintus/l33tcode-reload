class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        price_to_buy = prices[0]
        
        for day in range(1, len(prices)):
            if prices[day] < price_to_buy:
                price_to_buy = prices[day]
                continue
        
            profit = prices[day] - price_to_buy
            if profit > max_profit:
                max_profit = profit
        return max_profit
