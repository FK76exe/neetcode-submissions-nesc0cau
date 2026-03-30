class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sequences = {} # key = next number, # value = sequences
        nums = sorted(nums) # sort to make life easier
        for num in nums:
            if not sequences.get(num):
                if sequences.get(num+1):
                    continue # this to prevent duplicate numbers
                sequences[num+1] = [num]
            else:
                sequences[num].append(num)
                # change key
                sequences[num+1] = sequences[num]
                sequences.pop(num)
        # now get the biggest one
        longest_sequence_length = 0
        for i, sequence in enumerate(list(sequences.values())):
            if len(sequence) > longest_sequence_length:
                longest_sequence_length = len(sequence)
        return longest_sequence_length