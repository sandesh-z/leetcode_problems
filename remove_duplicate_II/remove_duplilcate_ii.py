#remove duplicate items if it occurence is more than 2
from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        copy = nums.copy()
        print(len(copy))
        for i,item in enumerate(copy):
            if(i>0 and i<len(copy)-1 and copy[i-1]==copy[i+1]):
                nums.remove(item)
        print(nums)        
        return len(nums)
    

s = Solution()
# test_list = [1,1,1,2,2,3]
# test_list = [0,0,1,1,1,1,2,3,3]
test_list = [1,1,1]
 
print(s.removeDuplicates(test_list))