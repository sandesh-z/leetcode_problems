from typing import List
import copy
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        cp = copy.deepcopy(matrix)
        m =len(cp[1])
        
        n = len(cp)
       
        for i in range (n):
            for j in range(m):
                if(cp[i][j]==0):
                    for k in range(m):
                        matrix[i][k] = matrix[i][k]*0
                    for l in range(n):    
                        matrix[l][j] = matrix[l][j]*0
                                   

                            

s = Solution()
# matrix =[[1,1,1],[1,0,1],[1,1,1]]
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
s.setZeroes(matrix)
print(matrix)

