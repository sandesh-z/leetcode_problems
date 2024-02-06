"""
Given an array of intervals where intervals[i] = [starti, endi],
merge all overlapping intervals,
and return an array of the non-overlapping intervals that cover all the intervals in the input.

Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
"""
from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        n = len(intervals)
        result = []
        result.append(intervals[0])
        for i in range(1,n):
            if not result:
                result.append(intervals[i])
            elif(intervals[i][0]>=result[-1][0] and intervals[i][0]<=result[-1][1]):
                a = result[-1][0]
                b = max(result[-1][1],intervals[i][1])
                del result[-1]
                result.append([a,b])
            else:
                result.append(intervals[i])    
        return result  


s = Solution()
# intervals = [[1,3],[2,6],[8,10],[15,18]]
# intervals = [[1,4],[4,5]]
# intervals =[[1,4],[2,3]]
# intervals  =[[1,4],[0,0]]
# intervals = [[0,0],[1,0]]
intervals = [[1,4],[0,2],[3,5]]
print(s.merge(intervals))         