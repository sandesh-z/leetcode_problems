class Solution:

   
    def isValid(self, s: str) -> bool:
 
     
        open_brackets = {'(', '{', '['}
        close_brackets = {')': '(', '}': '{', ']': '['}
        counter = {b: 0 for b in open_brackets}

        for char in s:
            if char in open_brackets:
                counter[char] += 1
            elif char in close_brackets:
                counter[close_brackets[char]] -= 1
                if counter[close_brackets[char]] < 0:
                    return False
            else:
                # Ignore characters that are not brackets
                continue

        # Check if all counters are zero
        return all(count == 0 for count in counter.values())
        
s=Solution()    
print(s.isValid("(]"))
print(s.isValid("{}()"))
print(s.isValid("()"))  
 
