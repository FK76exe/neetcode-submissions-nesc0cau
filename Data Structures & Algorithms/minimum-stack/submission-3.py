class MinStack:

    def __init__(self):
        self.stack = []
        # O(n) time complexity... meets recommendation
        self.ranked_stack = [] # sort in ascending order

        # had to use hints... let's see if it makes sense
        # a "prefix array" -> only stores min elements?
        self.prefix_array = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # add to ranked stack... but wouldn't that be O(n)?
        if len(self.prefix_array) != 0:
            self.prefix_array.append(min(val, self.prefix_array[-1]))
        else:
            self.prefix_array = [val]
        print(f"push {val}: {self.prefix_array}")

    def pop(self) -> None:
        self.stack.pop(-1)
        self.prefix_array.pop(-1)
        print(f"pop: {self.prefix_array}")

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        # pretty damn sure this is O(n)... needs to be better
        return self.prefix_array[-1]

"""
I get it...
Suppose the stack has n elements.
The prefix array would also have n elements

The ith element of the prefix array represents the minimum value of
the slice stack[:i] yields.

With the stack, we take advantage of the order control by keeping
the minimum for each slice of the stack anchored at 0.
"""
