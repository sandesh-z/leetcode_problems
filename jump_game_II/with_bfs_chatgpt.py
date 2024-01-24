from collections import deque
from typing import List
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)

        if n <= 1:
            return 0  # No jumps needed for an empty array or an array with only one element

        visited = [False] * n  # Keep track of visited indices
        queue = deque([(0, 0)])  # Queue to perform BFS, (index, jumps)

        while queue:
            current_index, jumps = queue.popleft()

            for i in range(current_index + 1, min(current_index + 1 + nums[current_index], n)):
                if not visited[i]:
                    if i == n - 1:
                        return jumps + 1  # Reached the last index, return the total number of jumps
                    visited[i] = True
                    queue.append((i, jumps + 1))

        return -1

           

s = Solution()
# test_list = [2,3,1,1,4]
test_list = [2,1]
# test_list = [2,3,0,1,4]
# test_list = [1,2,1,1,1]
# test_list = [2,0,2,0,1]
# test_list = [1,1,1,1,1]


print(s.jump(test_list))