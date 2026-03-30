class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Base Case -> if s <= 2 chars long, it's already biggest substring
        if len(s) < 2:
            return len(s)
        # set up window with length 1
        i = 0
        max_length = 0
        for j, char in enumerate(s):
            if j == 0:
                # this would yield a zero-length substring
                continue
            substring = s[i:j]
            # if the char is unique, substring length increases
            # be sure to compare new length with max_length
            if char not in substring:
                max_length = max(max_length, j - i + 1)
            # if it is... increment i until I find duplicate character
            # set i to char after it
            else:
                substring_index = s[i:j].index(char)
                i += substring_index + 1
                # had to add this... why?
                # "xxxxx" -> i will always equal j and length will always be 0
                # bc j boundary is exclusive, add 1
                max_length = max(max_length, j - i + 1)
        return max_length