from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cheapest = prices[0]
        maxProfit = 0
        sortedprice = (prices == sorted(prices))
        if(sortedprice):
            return prices[-1] -prices[0]
        for i,price in enumerate(prices):
            if(i==0):
                continue
            if(price<=cheapest):
                cheapest = price
            else:
                if(i!=len(prices)-1 and price>=prices[i+1]):
                    maxProfit = maxProfit+(price-cheapest)
                    cheapest = prices[i+1]   

                elif(i==len(prices)-1 and price>prices[-2]):
                  
                    maxProfit=maxProfit+price-cheapest
                       
    
        return maxProfit


s = Solution()
prices = [6,1,3,2,7,7]
# prices=[7,6,4,3,1]
# prices=[1,2,3,4,5]
# prices=[7,1,5,3,6,4]
# prices = [1,2,4,2,5,7,2,4,9,0]
print(s.maxProfit(prices))