# O(n) time/space is the goal... as is getting the thing correct

# naive approach: build a hash table and use direct addressing
# where key = element and value = occurences in nums
# O(n) space = extra allocation?
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_table = self.buildHashTable(nums)
        # using built-in sorting is O(nlogn)... how to beat that?
        # keep track of a leaderboard and update as we progress?
        top_k = [None]*k # each elem = (num, freq) -> this is O(1), right?
        for key in hash_table.keys():
            freq = hash_table[key]
            # go through top_k to see where it fits.
            # ... I'll make it its own function for readability
            top_k = self.updateLeaderboard(top_k, (key, freq))
        return [i[0] for i in top_k]

    def updateLeaderboard(self, leaderboard: list[tuple[int,int]], newEntry: tuple[int,int]
            ) -> list[tuple[int,int]]:
            elem, freq = newEntry
            for i, member in enumerate(leaderboard):
                # if freq is greater than member, place it and adjust list
                if member == None or freq > member[1]:
                    leaderboard[i+1:] = leaderboard[i:-1]
                    leaderboard[i] = newEntry
                    break
            return leaderboard

    def buildHashTable(self, nums: List[int]) -> dict[int,int]:
        elem_frequency = {}
        for num in nums:
            if elem_frequency.get(num):
                elem_frequency[num] += 1
            else:
                elem_frequency[num] = 1
        return elem_frequency