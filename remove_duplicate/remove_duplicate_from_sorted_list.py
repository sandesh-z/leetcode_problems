from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        copy = nums.copy()
        for i,item in enumerate(copy):
             if(i>0 and item==copy[i-1]):
                nums.remove(item)

        return len(nums)
    
s = Solution()
lists=[0,0,1,1,1,2,2,3,3,4]
s.removeDuplicates(lists)
