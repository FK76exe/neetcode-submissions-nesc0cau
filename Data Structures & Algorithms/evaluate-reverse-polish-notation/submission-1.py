class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # keep stack of operands
        # if digit: push
        # if sign: pop last two digits and apply operand. push result
        stack = [] 
        
        for token in tokens:
            try: # let's treat it like a number
                stack.append(int(token))
            except ValueError:
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(self.evalExpression(num1, num2, token))
            print(f"{token}: {stack}")
        return stack[0] # should be only one element

    def evalExpression(self, num1: int, num2: int, sign: str) -> int:
        # O(1)
        match sign:
            case '+':
                return num1 + num2
            case "-":
                return num1 - num2
            case "*":
                return num1 * num2
            case _: # division
                return int(num1 / num2)

"""
Time/Space Complexity? n = size of input array

For time: 
- stack operations and evalExpression are O(1)
- we have to iterate through all the tokens

therefore, O(n)

For space: we introduce a stack which can feature a lot of elements
O(n)
"""