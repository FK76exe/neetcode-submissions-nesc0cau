class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_elements = []
        # build window
        window = nums[:k]
        max_elements.append(max(window))
        # slide the window
        for i, num in enumerate(nums[k:]):
            # if prior max did not slide out, compare
            if window[0] != max_elements[-1]:
                max_elements.append(max(max_elements[-1], num))
                window.pop(0)
                window.append(num)
            # if prior max does slide out, sort again
            else:
                window.pop(0)
                window.append(num)
                max_elements.append(sorted(window, reverse=True)[0])
        return max_elements    