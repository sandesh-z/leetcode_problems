"""
Reverse bits of a given 32 bits unsigned integer
"""

class Solution:
    """
    In this function, we iterate through each bit of the input integer n from right to left.
    For each bit, we shift the result to the left by one bit (result << 1) 
    and then set the least significant bit of result to the current bit of n using bitwise OR operation |.
    Finally, we shift n to the right by one bit (n >>= 1).
    This process continues until all 32 bits are processed.
    """
    #code generated with chat gpt
    def reverseBits(self, n: int) -> int:
        result = 0
        for _ in range(32):
            result = (result << 1) | (n & 1)
            n >>= 1
        return result
    

s  = Solution()
print(s.reverseBits(43261596))    
