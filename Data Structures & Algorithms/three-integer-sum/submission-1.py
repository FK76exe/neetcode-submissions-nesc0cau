class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort()

        for i, num in enumerate(nums):
            # why? because this is a sorted array, meaning...
            # going further will be positive numbers -> greater than zero -> no triplets
            if num > 0:
                break
            # why are we skipping duplicates?
            # I was skipping duplicates when making triplet...
            # here... we do it while making our anchor. Makes sense,
            # since both numbers are looking at the same rightward range
            if i > 0 and num == nums[i-1]:
                continue
            
            j, k = i+1, len(nums) -1
            while j < k:
                threeSum = num + nums[j] + nums[k]
                if threeSum > 0:
                    k -= 1
                elif threeSum < 0:
                    j += 1
                else:
                    triplets.append([num, nums[j], nums[k]])
                    #  now what is this?!
                    # It's the same duplicate nonsense...
                    # here, we are moving j inward
                    j += 1
                    k -= 1
                    while nums[j] == nums[j-1] and j < k:
                        j += 1
        return triplets