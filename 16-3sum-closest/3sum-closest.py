class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        res = []
        mini = float('inf')
        ans = 0
        nums.sort()
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                a = nums[i] + nums[left] + nums[right]
                b = abs(target - a)
                if b < mini:
                    mini = b
                    ans = a
                if a < target:
                    left += 1
                else:
                    right -= 1
        return ans
