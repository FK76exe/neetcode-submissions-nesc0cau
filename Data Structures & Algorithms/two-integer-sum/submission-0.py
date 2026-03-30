class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # goal: find a pair of elements whose sum equals the target
        # how to make it less than O(n^2)? Cut out redundant searches
        # re hash table: put into slots where index is based on a function
        # key=number needed to pair with value?, value=previous number with index?
        # dict.get is O(1)
        
        hash_table = {} # each elem is a tuple (i, num)
        # construct hash table
        for i, num in enumerate(nums):
            if hash_table.get(num): # is there a compatible element with it?
                return [hash_table.get(num)[0], i]
            else:
                hash_table[target - num] = (i, num)
        # time complexity is O(n) -> no inner loop!