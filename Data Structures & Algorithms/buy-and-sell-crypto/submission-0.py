class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,1
        profit = 0
        while r<len(prices) :
            diff = prices[r] - prices[l]
            if diff<0:
                l = r
                r +=1
            elif diff>=0:
                profit = max(profit,diff)
                r+=1
        return profit
