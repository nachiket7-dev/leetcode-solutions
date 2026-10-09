class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        res = []
        res2 = []
        n = len(nums)
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                res.append(nums[i])
        for i in range(len(nums)):
            if nums[i] not in res:
                res2.append(nums[i])
        res2.sort(reverse=True)
        res.extend(res2)
        return res