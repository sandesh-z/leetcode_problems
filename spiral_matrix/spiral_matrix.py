"""
Given an m x n matrix, return all elements of the matrix in spiral order.

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
"""

from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        m = len(matrix)     #row
        n= len(matrix[0]) #column

        left =  up = down =right= False
        row,column = 0,0

        res = []
        #no spiral traversal need if all item of matrix contain only one column
        if n<=1:
            for i in range(m):
                res.append(matrix[i][0])

        total = (m*n) -1
        while len(res)<=total:

            if (column>=n-1 and right):
                n=n-1
                down = True
                left = right = up = False
            if row>=m-1 and down:
                m = m-1
                left = True
                right = up =down = False
            if row+column==len(matrix)-1 and row!=column and left:
                up = True 
                down = left = right = False
            if (row-column==1 and up) or (row==0 and column==0):
                right = True 
                left = up = down = False
                           
            if right:
                res.append(matrix[row][column])
                column+=1
            if left:
                res.append(matrix[row][column])
                column-=1
            if down:
                res.append(matrix[row][column])
                row+=1
            if up:
                res.append(matrix[row][column])
                row-=1   
        return res            



s = Solution()
# matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# matrix = [[3],[2]]
matrix =[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
print(s.spiralOrder(matrix))        

