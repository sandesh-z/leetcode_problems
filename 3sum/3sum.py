from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range (len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = -nums[i]
            left = i+1
           
            right = len(nums)-1
            while  left < right:

               

                if(nums[left]+nums[right]==target):
                    result.append([nums[i],nums[left],nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left=left+1
                    right = right -1
                elif(nums[left]+nums[right]<target):
                    left = left +1
                else:
                    right = right -1         
        return result            
       



s = Solution()
test_list = [-1,0,1,2,-1,-4]
# test_list=[0,1,1]
# test_list=[-2,0,0,2,2]
test_list = [-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0]
print(s.threeSum(test_list))
