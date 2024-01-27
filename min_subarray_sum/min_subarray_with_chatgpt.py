from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if target == 0:
            return 0

        length = 0
        left = 0
        current_sum = 0

        for right in range(len(nums)):
            current_sum += nums[right]

            while current_sum >= target:
                if length == 0:
                    length = right - left + 1
                else:
                    length = min(length, right - left + 1)

                current_sum -= nums[left]
                left += 1
                
        return length

s = Solution()
test_list = [2,3,1,2,4,3]
# test_list  = [1,4,4]
# test_list = [1,1,1,1,1,1,1,1]
print(s.minSubArrayLen(7,test_list))