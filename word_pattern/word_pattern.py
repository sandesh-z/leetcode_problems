class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(' ')
        test = zip(pattern,words)
        print(set(test))
        if  not len(words) == len(pattern):
            return False
        return len(set(zip(pattern, words))) == len(set(words)) == len(set(pattern))
    
s =Solution()
pattern = "aba" 
string = "dog dog cat"   
print(s.wordPattern(pattern,string))