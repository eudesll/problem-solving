class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = -inf
        l, r = 0, len(height) - 1
        while l < r:
            lowest_height = min(height[l], height[r])
            area = lowest_height * (r - l)
            maxArea = max(maxArea, area)

            if lowest_height == height[l]:
                l += 1
            else:
                r -= 1
        
        return maxArea