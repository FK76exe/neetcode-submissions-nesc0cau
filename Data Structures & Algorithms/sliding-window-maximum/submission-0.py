class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_elements = []
        # build window
        window = []
        for i in range(k):
            window.append(nums[i])
        max_elements.append(max(window))
        # slide the window
        for i, num in enumerate(nums[k:]):
            window = window[1:k] + [num]
            max_elements.append(max(window))
        return max_elements    