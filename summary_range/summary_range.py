from typing import List
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)
        ranges = []
        if(n<=1):
            if(n<1):
                return ranges
            else:
                ranges.append(str(nums[0]))  
                return ranges
        a = nums[0]
        b = nums[1]
        for i,num in enumerate(nums):
            if(i<len(nums)-1 and abs(nums[i]-nums[i+1])>1): 
                b = num  
                if(a==b):
                    ranges.append(str(a))
                else:
                    ranges.append(str(a)+"->"+str(num))
                if i<n-1:
                    a = nums[i+1]    
            elif(i==n-1):
                if(abs(nums[i]-nums[i-1])>1):
                    ranges.append(str(num))
                else:
                    ranges.append(str(a)+"->"+str(num))
     
        return ranges

s = Solution()
# nums = [0,1,2,4,5,7]
# nums = [0,2,3,4,6,8,9]
nums = [1]
print(s.summaryRanges(nums))