# with time complexity 0(n^2)
import timeit
from typing import List
start = timeit.default_timer()

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
       
        result = []
       
        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if(nums[j]==nums[i] and i==j):
                    continue
                product = product*nums[j]
           
            result.insert(i,int(product))

        return result

testList = [1,2,3,4]  
s = Solution()
print(s.productExceptSelf(testList))  

stop = timeit.default_timer()

print('Time: ', stop - start) 
print(7.589399956486886e-05-7.589399956486886e-05)