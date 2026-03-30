class Solution:
    def isPalindrome(self, s: str) -> bool:
        # preprocessing
        s = s.replace(" ", '').lower()
        # loop
        i = 0
        j = len(s) - 1
        while j > i:
            # can I bypass non-alphanumeric characters here?
            if not s[i].isalnum():  
                i += 1
            elif not s[j].isalnum():
                j -= 1
            elif s[i] != s[j]:
                return False
            else:
                i += 1
                j -= 1
        return True
