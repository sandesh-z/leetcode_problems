from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        copy = nums.copy()
        for item in copy:
            if(item==val):
                nums.remove(item)

        return len(nums) 

s= Solution()
arr = [0,1,2,2,3,0,4,2]
print(s.removeElement(arr,2))
    