from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        
        # if n == 1 and digits[0] == 9:
        #     return [1, 0]
        
        for i in range(n - 1, -1, -1):
            if digits[i] + 1 == 10:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        
        digits.insert(0, 1)
        return digits
    
s = Solution()
testList = [0]
print(s.plusOne(testList))