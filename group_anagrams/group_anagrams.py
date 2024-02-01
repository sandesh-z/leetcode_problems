from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = {}
        for item in strs:
            sorted_str =  "".join(sorted(item))
            if(sorted_str in anagram_dict):
                anagram_dict[sorted_str].append(item)
            else:    
                anagram_dict[sorted_str] = [item] 
        result = [value for value in anagram_dict.values()] 
        return result       
        # return list(anagram_dict.values()) 

s= Solution()
anagrams = ["eat","tea","tan","ate","nat","bat"]
# anagrams = ["a"]
print(s.groupAnagrams(anagrams))           