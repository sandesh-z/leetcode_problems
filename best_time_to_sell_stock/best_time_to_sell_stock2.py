from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cheapest = prices[0]
        maxProfit = 0
        for price in prices[1:]:
            if(price<cheapest):
                cheapest = price
            elif(maxProfit<price-cheapest):
                maxProfit = price-cheapest            
                
        return maxProfit


s = Solution()
prices = [7,1,5,3,6,4]
p2 = [1,4,3,2,4,8,4]
p3=[2,1]
p4 = [2,1,2,0,1]
print(s.maxProfit(p4))
