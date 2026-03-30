# Performance Goal: O(m*n) time, m = # of strings, n = len(longest string)
# Space Goal: O(m), m = # of strings

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramDict = {}
        for string in strs:
            key = self.generateHashKey(string)
            dictSearchResult = anagramDict.get(key)
            if dictSearchResult:
                anagramDict[key].append(string)
            else:
                anagramDict[key] = [string]
        return list(anagramDict.values())
    
    def generateHashKey(self, string: str) -> str:
        # hash fn: return an alphabetically sorted 
        # string with all characters from "string"
        # NOTE: strings with same key must be grouped together
        return ''.join(sorted(list(string)))