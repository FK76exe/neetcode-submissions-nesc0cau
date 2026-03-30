class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) == 0:
            return ""
        countT = {}
        for char in t:
            countT[char] = 1 + countT.get(char, 0)

        window = {}
        have = 0
        need = len(countT)
        res, resLen = [-1, -1], float("infinity")
        l = 0
        for r, char in enumerate(s):
            window[char] = window.get(char, 0) + 1
            if char in countT and window[char] == countT[char]:
                have += 1
            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r+1] if resLen != float("infinity") else ""