class Solution:
    def isValid(self, s: str) -> bool:
        bracketStack = [] # open brackets only. Pop when most recent bracket
        pairs = {'}': '{', ')': '(', ']': '['}
        # is closed
        for char in s:
            if char in ['(', '[', '{']:
                bracketStack.append(char)
            else:
                opening_bracket = pairs[char]
                if len(bracketStack) == 0:
                    return False
                if opening_bracket != bracketStack[-1]:
                    return False
                bracketStack.pop(-1)
        return len(bracketStack) == 0

"""
We need to keep track of any open brackets that haven't been closed
Idea: three bool vars -> isSquareopen, isParen open, is curly open, isround open
- no need to check entire stack when we have handy variables
"""