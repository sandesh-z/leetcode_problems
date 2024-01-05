from typing import List


        
class Solution:
    def findNLargestOrSmallest(self,prices:List[int],n,findSmallest =False)-> int:
        if(n>len(prices)-1 or n<=0):
            return -1
        count =1
        largest = prices[0]
        for price in prices:
            if(price<largest and findSmallest):
                largest = price
            elif(price>largest and not findSmallest):
                largest = price
            elif(price==largest):
                largest = price        
        if(count==n):
            return largest
        else:        
            count+1
            prices.remove(largest)
            return self.findNLargestOrSmallest(prices,n-1,findSmallest)
    def maxProfit(self, prices: List[int]) -> int:
        if(len(prices)==1):
            return 0
        iteration = 1
        max = self.findNLargestOrSmallest(prices,iteration)
        min = self.findNLargestOrSmallest(prices,iteration,True)

        max_index = prices.index(max)
        min_index = prices.index(min)
        
        last_item = prices[-1]
    
        if(prices[min_index]==last_item and len(prices)>2):
            min = self.findNLargestOrSmallest(prices,2,True)
            min_index = prices.index(min)

        while max_index<min_index:
            iteration = iteration+1
            if(iteration>=len(prices)):
                return 0
            max = self.findNLargestOrSmallest(prices,iteration)
            max_index = prices.index(max)
            print(max_index)

     
        return max-min

         
s = Solution()
prices = [7,1,5,3,6,4]
p2 = [1,4,3,2,4,8,4]
p3=[2,1]
p4 = [2,1,2,0,1]
print(s.maxProfit(p4))

