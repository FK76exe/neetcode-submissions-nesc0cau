"""
So... I fucked up.
Things were too complicated -> 80+ LoC..

- didn't handle duplicates (advice: use a set)
"""

# using Neetcode solution
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # mp key = num, val = sequence length starting at num?
        mp = defaultdict(int) # default key of 0 (if missing key)
        answer = 0

        for num in nums:
            if not mp[num]:
                # num combines length of neighbours + 1 (bridging a gap)
                # if a neighbour doesn't have a sequence, it's still 0
                mp[num] = mp[num-1] + mp[num+1] + 1
                # propagate info to neighbours
                mp[num-mp[num-1]] = mp[num]
                mp[num+mp[num+1]] = mp[num]
                # update answer
                answer = max(answer, mp[num])
            print(f"After {num}: {mp}")
        return answer

"""
What's the philosophy here?
- it's not like solitaire
- it's a number line and the only thing affected are the neighbours?
"""