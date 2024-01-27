#this solution exceeds time limits
from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if(target==0):
            return 0
        length = 0
        r = len(nums)-1
        for i in range(len(nums)):
            if(nums[i]==target):
                length = 1
                break
            currentSum = 0
            for j in range(i,len(nums)):
                currentSum+=nums[j]
                if(currentSum>=target):
                    if(length==0):
                        length = j-i+1
                    else:    
                        length = min(length,j-i+1)
                    break

        return length


s = Solution()
test_list = [2,3,1,2,4,3]
# test_list  = [1,4,4]
# test_list = [1,1,1,1,1,1,1,1]
print(s.minSubArrayLen(7,test_list))