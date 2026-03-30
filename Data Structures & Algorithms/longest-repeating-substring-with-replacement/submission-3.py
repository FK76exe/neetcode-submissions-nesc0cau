class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = 0
        max_length = 0
        for j, letter in enumerate(s):
            if j == 0:
                # empty substring
                continue
            substring = s[i:j] + letter
            dominant_letter = self.findDominantLetter(substring)
            # does the letter change substring's adherence to window 
            # constraint?
            print(substring)
            if substring.count(dominant_letter) + k >= len(substring):
                # it's good? compare with tally and move on
                max_length = max(max_length, len(substring))
            else:
                # time to change out
                while i <= j and substring.count(dominant_letter) + k < len(substring):
                    i += 1
                    substring = s[i:j] + letter
                    dominant_letter = self.findDominantLetter(substring)
                    print(i, j, dominant_letter, substring)
                # condition reinstated? check max length again
                max_length = max(max_length, len(substring))
        return max_length

    
    def findDominantLetter(self, s: str) -> str:
        """Get the dominant letter. If a tie, return first one"""
        letter_count = {}
        for letter in s:
            if letter_count.get(letter) is None:
                letter_count[letter] = 1
            else:
                letter_count[letter] += 1
        # dumbass intellisense... learned new tip tho!
        return max(letter_count, key=letter_count.get)
