from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
         max_reach = 0
         n = len(nums)

         for i in range(n):
            # Check if it's possible to reach the current index
            if i > max_reach:
                return False
            
            # Update the maximum reach if a longer jump is possible
            max_reach = max(max_reach, i + nums[i])

            # If the maximum reach is greater than or equal to the last index, return true
            if max_reach >= n - 1:
                return True

         return False

s = Solution()
# mylist = [2,3,1,1,4]

# mylist = [3,3,1,2,4]
# mylist=[3,2,1,0,4]
# mylist =[2, 4, 1, 1, 0, 2, 3]
mylist = [3,1,1]
print(s.canJump(mylist))    