"""
Given two strings ransomNote and magazine,
return true if ransomNote can be constructed
by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.
"""
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for r in ransomNote:
            if r in magazine:
                magazine = magazine.replace("a","",1)
            else:
                return False     
        return True            
        


s = Solution()
r = "aa"
m = "ab"
print(s.canConstruct(r,m))        