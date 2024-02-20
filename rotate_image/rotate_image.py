"""
You are given an n x n 2D matrix representing an image,
rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place,
which means you have to modify the input 2D matrix directly.
DO NOT allocate another 2D matrix and do the rotation

Constraints:
n == matrix.length == matrix[i].length
1 <= n <= 20
-1000 <= matrix[i][j] <= 1000
"""

from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                #transpose matrix
                if i!=j and j>i:
                    matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
            #reverse every row        
            matrix[i].reverse()           
        

s = Solution()
matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# matrix = [[1,2,3],[4,5,6],[7,8,9]]
s.rotate(matrix)
print(matrix)       