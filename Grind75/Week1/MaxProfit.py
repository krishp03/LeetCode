class MaxProfit:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0

        l, r = 0, 1
        while r < len(prices):
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
            else:
                l = r
            r+=1
        return maxProfit
      
