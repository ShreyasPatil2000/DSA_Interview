from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        max_profit = 0
        min_price = prices[0]
        for price in prices[1:]:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)
        return max_profit

ob = Solution()
print(ob.maxProfit([7, 1, 5, 3, 6, 4]))
    
# First we check if prices are there or length of prices is less than 1. We initialize max profits to 0 and min price to prices[0]. We iterate through the next items in prizes through for loop. If price is less than min price then we set that to minimum. If its greater then we check for max profit. At the end we return max profit

# Time Complexity: O(N) as iterating through a for loop takes that much time. 
# Space Complexity: O(1) as we are storing constants.