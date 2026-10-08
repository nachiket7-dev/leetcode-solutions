class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        st = 0
        end = n - 1
        while st <= end:
            mid = (st + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                st = mid + 1
            else:
                end = mid - 1
        return st