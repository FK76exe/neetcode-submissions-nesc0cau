class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]*len(temperatures)
        waitingList = [] # stack
        for i, temp in enumerate(temperatures):
            if i == 0:
                waitingList.append(i) # hold index
            else: # evaluate
                while temp > temperatures[waitingList[-1]]:
                    day = waitingList.pop(-1)
                    result[day] = i - day
                    if len(waitingList) == 0:
                        waitingList.append(i)
                        break
                waitingList.append(i)
        return result

"""
So my main confusion is how do I "look back" at previous days?
Suppose I am at day A.
Then I encounter day B at some later point
if day B is warmer, then we have to wait N days for a future day.
else: keep going.

Easy way is to brute force but we need O(n)... how?
I can store auxillary data in a sep stack/array? Like max "temp" over N days

now with the temperature stack... can we compare?

--- after seeing solution ---
man i am so stupid.
use the stack for days waiting for a future warmer day
when we do so, we can pop the day and compute the number of days

USE WHITEBOARD
"""
        