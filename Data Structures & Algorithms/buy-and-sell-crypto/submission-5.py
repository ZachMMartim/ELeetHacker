class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        currBuy = prices[0]

        for price in prices: 
            maxProfit = max(maxProfit, price - currBuy)
            currBuy = min(currBuy, price)

        return maxProfit

       