from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        new_nums = list(sorted(numset))
        count=1
        n = len(new_nums)
      
        if(n<=1):
            return 0 if n<1 else 1
        map={}
        for i in range(1,n):
            if(abs(new_nums[i]-new_nums[i-1])<=1):
                count+=1
                if(i==n-1):
                   map[i]=count 
            else:
                map[i-1]=count
                count = count*0 + 1 
        return max(map.values())        








s = Solution()
# nums = [100,101,4,200,1,3,2]
nums = [100,101,102,103,104,105,4,200,1,3,2]
# nums = [0,3,7,2,5,8,4,6,0,1]
# nums = [0,-1]
# nums = [100,200,300]
# nums = [9,1,4,7,3,-1,0,5,8,-1,6]
print(s.longestConsecutive(nums))