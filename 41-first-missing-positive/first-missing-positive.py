class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        n = len(nums)
        for i in range(n + 1):
            d[i] = 0
        for i in nums:
            if i in d:
                d[i] += 1
        for i in d:
            if d[i] == 0 and i > 0:
                return i
        return n + 1
