class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # s & t are anagrams if they use the same set of characters
        # if we sort both strings... it should be the same sequence of characters
        return sorted(list(s)) == sorted(list(t))