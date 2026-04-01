class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums)-1 # search area boundaries; j-- -> otherwise indexerror
        while i <= j: # if i > j, then search area is effectively zero
            # remember to add the left boundary as an offset!
            mid_index = ((j-i) // 2) + i # floor division
            print(i, j, mid_index)
            median = nums[mid_index]
            if median < target:
                # limit search area to right half
                # add 1 to omit median from new search area
                i = mid_index + 1
            elif median > target:
                # limit search area to right half
                # remove 1 to omit median from new search area
                j = mid_index - 1
            else:
                return mid_index
        return -1
