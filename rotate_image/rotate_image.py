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
        # for i in range(len(matrix)):
        #     for j in range(len(matrix)):
        #         #transpose matrix
        #         if i!=j and j>i:
        #             matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        #     #reverse every row        
        #     matrix[i].reverse()

        """with utilization of built-in method zip this can be done in one line as:"""
        # matrix[:] = zip(*matrix[::-1])    

            
    def rotateAntiClockWise(self,matrix:List[List[int]])-> None:
        n = len(matrix)
        for i in range(n):
            for j in range(n):
                #mirror matrix along secondary diagonal
                if i+j!=n-1 and i+j<n-1:
                    matrix[i][j],matrix[n-1-j][n-1-i]=matrix[n-1-j][n-1-i],matrix[i][j]
            #reverse every row        
            matrix[i].reverse()                     
        

s = Solution()
matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# matrix = [[1,2,3],[4,5,6],[7,8,9]]
s.rotateAntiClockWise(matrix)
# s.rotate(matrix=matrix)
print(matrix)       