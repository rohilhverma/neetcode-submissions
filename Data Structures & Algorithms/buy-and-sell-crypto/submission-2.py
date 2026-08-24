class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit=0

        for x in range(len(prices)):
            y=x+1
            while y<len(prices):
                if prices[y]>prices[x]:
                    profit=max(prices[y]-prices[x], profit)
                y+=1
            
        return profit