class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = "".join([ch for ch in s if ch.isalpha() or ch.isdigit()]).lower()
        if(res==res[::-1]):
            return True
        return False    
    
s= Solution()

testStr ="A man, a plan, a canal: Panama"

print(s.isPalindrome(testStr))    