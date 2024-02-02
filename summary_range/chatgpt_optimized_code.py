from typing import List
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)
        ranges = []

        if n <= 1:
            return [str(nums[0])] if n == 1 else ranges

        start, end = nums[0], nums[0]

        for i in range(1, n):
            if abs(nums[i] - nums[i-1]) > 1:
                end = nums[i-1]
                ranges.append(str(start) if start == end else f"{start}->{end}")
                start = nums[i]

        end = nums[-1]
        ranges.append(str(start) if start == end else f"{start}->{end}")

        return ranges

s = Solution()
# nums = [0,1,2,4,5,7]
# nums = [0,2,3,4,6,8,9]
nums = [1]
print(s.summaryRanges(nums))