from itertools import combinations as comb
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        arr = []
        n = len(nums)
        for i in range(n + 1):
            ls = [list(j) for j in comb(nums, i)] 
            arr.extend(ls)
        return arr