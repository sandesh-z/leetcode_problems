import timeit
from typing import List
start = timeit.default_timer()
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        #create porduct list and initialize with 1's eg: [1,1,1,1]
        product = [1]*length

        #product of left elements from ith element of nums and ith element of product
        for i in range(1,length):
            product[i] = product[i-1]*nums[i-1]

        #calculate right products and multiply with left products    
        right = nums[-1]
        for j in range(length-2,-1,-1):
            product[j]*=right
            right *=nums[j]
        return product



s = Solution()
testList = [1,2,3,4]
print(s.productExceptSelf(testList))

stop = timeit.default_timer()
print('Time: ', stop - start)