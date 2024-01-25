from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        n = len(nums)
        for i in range(n):
            for j in range(i,n):
                for k in range(j,n):
                    if(i!=j and i!=k and j!= k):
                        if(nums[i] + nums[j] + nums[k] == 0):
                            temp_list = sorted([nums[i],nums[j],nums[k]])
                            my_tuple = tuple(temp_list)
                            res.add(my_tuple)
                            
        my_list = list(res)
        final_list = []
        for item in my_list:
            temp_list = list(item)
            final_list.append(temp_list)
        return final_list

s = Solution()
test_list = [-1,0,1,2,-1,-4]
print(s.threeSum(test_list))
