class Solution:
    def trap(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        bottleneck = 0 # shortest height of the bar
        area = 0
        while i < j:
            # calculate area: width * extra spaces added
            area += (j-i-1) * max(min(height[i], height[j]) - bottleneck, 0)
            # remember: think in terms of layers
            # If we added new spaces -> increase the bottleneck
            if min(height[i], height[j]) > bottleneck:
                bottleneck = min(height[i], height[j])
            
            # traverse -> move smaller of the bars, else both
            # if they haven't converged, subtract area as the bars may take up space
            if height[i] < height[j]:
                i += 1
                if i < j:
                    area -= min(height[i], bottleneck)
            elif height[j] < height[i]:
                j -= 1
                if i < j:
                    area -= min(height[j], bottleneck)
            else:
                i += 1
                if i < j:
                    area -= min(height[i], bottleneck)
                j -= 1
                if i < j:
                    area -= min(height[j], bottleneck)
        return area