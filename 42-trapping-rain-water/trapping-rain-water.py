class Solution:
    def trap(self, height: list[int]) -> int:
        ans = 0
        n = len(height)
        left = 0
        right = n - 1
        leftMax = 0
        rightMax = 0
        while left <= right:
            if height[left] < height[right]:
                leftMax = max(leftMax,height[left])
                ans += leftMax - height[left]
                left += 1
            else:
                rightMax = max(rightMax,height[right])
                ans += rightMax - height[right]
                right -= 1
        return ans