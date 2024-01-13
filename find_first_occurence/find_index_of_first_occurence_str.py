class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
    
s = Solution()
haystack = "sadbutsad"
needle = "sad"    

s.strStr(haystack,needle)