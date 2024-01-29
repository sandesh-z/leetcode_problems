from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
            """
            Do not return anything, modify matrix in-place instead.
            """
            copy = matrix.copy()
            m =len(copy[1])
           
            n = len(copy)
            
            for i in range (n):
                for j in range(m):
                    # print("i,j" ,copy[i][j])
                    if(copy[i][j]==0):
                      
                        if(i==1 and j==1):
                           
                            matrix[i-1][j]*=0  
                            matrix[i][j-1]*=0                          
                            matrix[i+1][j]*=0
                            matrix[i][j+1]*=0
                            

s = Solution()
matrix =[[1,1,1],[1,0,1],[1,1,1]]
s.setZeroes(matrix)
print(matrix)
