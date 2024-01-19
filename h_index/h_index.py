from typing import List
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        h = 0
        for item in citations:
            if(h>=item):
                return h
            h = h+1
        return h
s = Solution()
# mylist =[3,0,6,1,5]
# mylist =[1,3,1]
mylist = [25, 20, 15, 10, 8, 7, 6, 5, 3, 2]

print(s.hIndex(mylist))