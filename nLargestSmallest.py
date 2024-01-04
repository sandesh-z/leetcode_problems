from typing import List
def findNLargestOrSmallest(self,nList:List[int],n,findSmallest =False)-> int:
        if(n==1):
             return nList[0]
        if(n>len(nList)-1 or n<=0):
            return -1
        count =1
        largest = nList[0]
        for price in nList:
            if(price<largest and findSmallest):
                largest = price
            elif(price>largest and not findSmallest):
                largest = price    
        if(count==n):
            return largest
        else:        
            count+1
            nList.remove(largest)
            return self.findNLargestOrSmallest(nList,n-1,findSmallest)