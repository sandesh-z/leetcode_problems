class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        try:
            return haystack.index(needle)
        except:
            return -1
s = Solution()
haystack = "sadbutsad"
needle = "sad"    

s.strStr(haystack,needle)