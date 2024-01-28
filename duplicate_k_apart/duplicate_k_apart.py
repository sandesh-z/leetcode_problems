from typing import List
import timeit
start = timeit.default_timer()
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        #solution with o(n^2) complexity
        # if(len(nums)==1):
        #     return False
        # for i in range(len(nums)):      
        #     for j in range(i+1,k+i+1):
        #         if(j<len(nums) and nums[i]==nums[j] and abs(i-j)<=k):
        #             return True
        # return False
       
        index_dict = {}

        for i, num in enumerate(nums):
            if num in index_dict and i - index_dict[num] <= k:
                return True
            index_dict[num] = i

        return False
    
s = Solution()
# test_list = [1,2,3,1]  
# test_list = [-1,-1]
test_list = [1,0,4,3,7,6,5,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,1]
print(s.containsNearbyDuplicate(test_list,1)) 
stop = timeit.default_timer()
print('Time: ', stop - start)