class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i=0
        j=0
        
        while j<len(t):
            if(i<len(s) and s[i]==t[j]):
                i=i+1
            j+=1    

        return i==len(s)
        

s = Solution()
substr = "abc"
teststr = "ahbgdc"
print(s.isSubsequence(substr,teststr))