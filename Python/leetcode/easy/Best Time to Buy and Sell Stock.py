"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a 
different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        
        for price in prices[1:]:
            max_profit = max(max_profit, price - min_price)
            min_price = min(min_price, price)
            
        return max_profit


prices = [7,1,5,3,6,4]
thingy = Solution()
print(thingy.maxProfit(prices))

"""        for i, price in enumerate(prices):
            if price < self._low and self._high in prices[i:]:
                self._low = price
            elif price > self._high:
                if price in prices[i:]:
                    self._high = price"""