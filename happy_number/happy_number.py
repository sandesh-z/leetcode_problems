class Solution:
    def isHappy(self, n: int) -> bool:
        num = str(n)
        dict={}
        while n>0:
            count = 0
            total = 0
            for item in num:
                product = int(item) * int(item)
                total += product
            if(total in dict):
                return False  
            elif(total==1):
                return True 
            else:
                dict[total]=count+1  
            num =str(total)
       

s = Solution()
print(s.isHappy(1111111))

