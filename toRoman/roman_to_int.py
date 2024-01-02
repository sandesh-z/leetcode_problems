import timeit

start = timeit.default_timer()
class Solution(object):
    def sum(self,char):
        sum = 0
        match char:
                case "I":
                    return sum+1
                case "V":
                    return sum+5
                case "X":
                    return sum+10
                case "L":
                    return sum+50
                case "C":
                    return sum+100
                case "D":
                    return sum+500
                case "M":
                    return sum+1000

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum = 0
        if (len(s)==1):
            return self.sum(s)
        else:
            for index,char in enumerate(s):
                if index < len(s) - 1 and s[index] == "I" and s[index+1]=="V":
                    sum=sum+4
                elif index > 0 and s[index] == "V" and s[index-1]=="I":
                    continue
                elif index < len(s) - 1 and s[index] == "I" and s[index+1]=="X":
                    sum=sum+9
                elif index>0 and s[index]=="X" and s[index-1]=="I":
                    continue
                elif index < len(s) - 1 and s[index] == "X" and s[index+1]=="L":
                    sum=sum+40
                elif index>0 and s[index]=="L" and s[index-1]=="X":
                    continue
                elif index < len(s) - 1 and s[index] == "X" and s[index+1]=="C":
                    sum=sum+90
                elif index>0 and s[index]=="C" and s[index-1]=="X":
                    continue
                elif index < len(s) - 1 and s[index] == "C" and s[index+1]=="D":
                    sum=sum+400
                elif index>0 and s[index]=="D" and s[index-1]=="C":
                    continue
                elif index < len(s) - 1 and s[index] == "C" and s[index+1]=="M":
                    sum=sum+900
                elif index>0 and s[index]=="M" and s[index-1]=="C":
                    continue
                else:
                    sum = sum+self.sum(char)
            return sum

                    
solution = Solution()

   
solution = Solution()
with open("text.txt","r") as file:
    for line in file:
        print(solution.romanToInt(str(line.strip())))

stop = timeit.default_timer()

print('Time: ', stop - start)         