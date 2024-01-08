from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        majority_index = 0
        majority = 0
        for i,item in enumerate(nums):
            if(i>0 and item==nums[i-1]):
                continue
            if(nums.count(item)>majority):
                majority=nums.count(item)
                majority_index=i
            
            
        return nums[majority_index]        





s = Solution()

test2 = [4,6,6,6,7,7]
print(s.majorityElement(test2))

        