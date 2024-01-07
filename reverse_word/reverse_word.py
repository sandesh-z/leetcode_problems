class Solution:
    def reverseWords(self, s: str) -> str:
        rStr =""
        for i in s:
            if(i!=" "):
                rStr+=i
            else:
                rStr+=" "
                continue

         
        temp = rStr.split()
        temp.reverse()
        return " ".join(str(x) for x in temp)
         


s = Solution()
print(s.reverseWords("hello world"))