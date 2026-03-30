import string

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # first, build letter array for s1
        # pre sure because ascii is fixed-size, it's O(1)
        # its size does not scale with input
        s1_letters = [0]*26
        for char in s1:
            s1_letters[self.getCharIndex(char)] += 1
        # build s2's letter array and window
        print(s1_letters)
        print("-cut-")
        window_letters = [0]*26
        for i, char in enumerate(s2):
            # first, let's assemble the window
            # if i is less than s1, just add, don't remove
            window_letters[self.getCharIndex(char)] += 1
            # otherwise we have to decrement an outgoing character's count
            if i >= len(s1):
                window_letters[self.getCharIndex(s2[i-len(s1)])] -= 1
            print(window_letters)
            # compare letter arrays -> s1 is permutation of substring
            # contained in window if letter arrays are equal
            if window_letters == s1_letters:
                return True
        return False

    def getCharIndex(self, char: str):
        return string.ascii_lowercase.index(char)