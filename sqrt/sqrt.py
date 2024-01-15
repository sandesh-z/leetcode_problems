class Solution:
    def mySqrt(self, x: int) -> int:
        count=0
        res = 1
        while res>0:
            if(res<0):
                return count
            res = x-(2*count+1)
            x = res
            if(res<0):
                return count
            count = count+1
            if(res==0):
                return count
    
        return count
s = Solution()
print(s.mySqrt(8))    