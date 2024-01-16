from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        mylist = []
        start = 0
        end = len(numbers)-1
        while numbers[start]<=numbers[end]:
            if(numbers[start]+numbers[end]==target):
                mylist.append(start+1)
                mylist.append(end+1)
                return mylist
            elif(numbers[start]+numbers[end]<target):
                start = start +1
            else:
                end = end -1   

s= Solution()
testList = [2,7,11,15]
print(s.twoSum(testList,target=9))