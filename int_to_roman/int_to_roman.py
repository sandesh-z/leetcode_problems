
class Solution:    
    def intToRoman(self, num: int) -> str:
        hmap = {
            1:    'I',
            4:    'IV',
            5:    'V',
            9:    'IX',
            10:    'X',
            40:    'XL',
            50:    'L',
            90:    'XC',
            100:    'C',
            400:    'CD',
            500:    'D',
            900:    'CM',
            1000:    'M'
        }
        arr= [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        res=""

        while num>0:
            i = 0
            while arr[i]>num:
                i+=1
            num = num-arr[i]
            res = res+ hmap[arr[i]]
            i+=1 
        return res    
    
s = Solution()
print(s.intToRoman(1999))    
        
