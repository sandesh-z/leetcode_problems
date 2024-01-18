from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.

        """
        
        nums1[0:m+n] = sorted(nums1[:m]+nums2[:n])

        print(nums1)        

s = Solution()
# nums1 =  [1,2,3,4,0,0,0]
# nums2 = [2,5,6]
nums1 =  [1,2,4,5,6,0]
nums2 = [3]
print(nums1[:5]+nums2[:1])
print(nums1)
print(nums1[:5])

# nums1 =  [2,0]
# nums2 = [1]
s.merge(nums1,5,nums2,1)