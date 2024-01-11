from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        copy = nums.copy()
        for i in range(len(copy)):
            if(i+k>=len(copy)-1):
                shift = (i+k)%len(copy)
                print(shift)
            else:
                shift = i+k  
            nums[shift] = copy[i]
                
           
                    
nums = [1,2,3,4,5,6,7]
s = Solution()
s.rotate(nums,3)
print(nums)
