class Solution:
    # Approach: get nums by multiplying everything and then make output
    # by dividing master number by each index
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        masterProduct = 1
        zeroTally = 0
        zerolessMasterProduct = 1
        for i in nums:
            masterProduct *= i
            if i != 0:
                zerolessMasterProduct *= i
            else:
                zeroTally += 1
        output = [0]*len(nums)
        if zeroTally > 1:
            return output
        for i, num in enumerate(nums):
            if num == 0:
                output[i] = zerolessMasterProduct
            if masterProduct == 0:
                continue
            else:
                output[i] = int(masterProduct / num)
        return output

# Goal: Return array output where output[i] is the product of all elements of
# nums except nums[i]

# Goal is O(n)

# issue with zero
# once you divide by zero, it cannot be reversed... how to handle?
# 0 is basically a black hole. Once it is encountered, everything will be zero.
# there can be multiple zeros...
# how about... we keep track of zeros?
# if one zero exists -> we have the "zeroless" number
# if two or more -> answer will always be zero