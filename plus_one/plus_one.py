from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        end = len(digits) -1
        if(len(digits)==1):
            if(digits[end]==9):
                return [1,0]
            else:
                digits[end]= digits[end]+1
                return digits
        else:
            while end>=0:
                if(digits[end]+1==10):
                    if(end==0 and digits[end+1]==0):
                        digits[end]=0
                        digits.insert(0,1)
                    elif(end!=0):    
                        digits[end]=0 
                else:    
                    digits[end]=digits[end]+1
                    if(digits[end]<10):
                        break
                end=end-1    
        return digits            
           
    
s = Solution()
testList = [9]
print(s.plusOne(testList))