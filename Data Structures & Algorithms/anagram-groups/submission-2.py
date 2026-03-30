# Solution 1 time performance was O(m*nlogn)... what's the slowdown?
# hash key generation is O(nlogn)... so hash key generation has to be O(n),
# where O(n) is longest string...
import string

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
    
    def generateHashKey(self, word: str) -> str:
        # per hint and my intuition: store frequency as an array...
        # that's the hash key
        alphabet = string.ascii_lowercase
        key = [0]*26
        for char in word:
            position = alphabet.find(char)
            key[position] += 1
        return '-'.join([str(i) for i in key])
        