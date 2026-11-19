class Solution:
    def maxArea(self, height: list[int]) -> int:
        l,r = 0,len(height) - 1
        area = float("-inf")
        while l <= r:
            a = min(height[l],height[r]) * (r - l)
            area = max(area,a)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return area