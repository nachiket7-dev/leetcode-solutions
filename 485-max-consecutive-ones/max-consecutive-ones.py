class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxi = 0
        ct = 0
        for i in nums:
            if i == 1:
                ct += 1
            else:
                maxi = max(maxi,ct)
                ct = 0
        maxi = max(maxi,ct)
        return maxi