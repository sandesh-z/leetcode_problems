"""Given an integer numRows, return the first numRows of Pascal's triangle."""
from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        if numRows==0:
            return []
        if numRows==1:  
            return [1]
        if numRows==2:
            return [1,1]

        for i in range(1,numRows+1):
            row = [1]*i
            for j in range(1,len(row)+1):
                if j==1 or j==len(row):
                    pass
                else:
                    print(i,j)
                    row[j-1] = res[i-2][j-1]+res[i-2][j-2]
            res.append(row)    

        return res      
        
s=Solution()
print(s.generate(5))        