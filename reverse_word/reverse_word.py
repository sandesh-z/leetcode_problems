class Solution:
    def reverseWords(self, s: str) -> str:
        temp = s.split()
        temp.reverse()
        return " ".join(str(x) for x in temp)
         


s = Solution()
print(s.reverseWords("hello world"))