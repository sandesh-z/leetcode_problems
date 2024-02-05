"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.
"""
"""
1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.
"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map = {}
        if len(t)==0 or len(t)==0:
            return False
        for i,item in enumerate(s):
            if (item in map and map[item]!=t[i]) or (item not in map and t[i] in map.values()):
                return False
            map[item]= t[i]

        return True

s= Solution()
# str1= "paper"
# str2= "title"
str1 = "badc"
str2 = "baba"

print(s.isIsomorphic(str1,str2))
            