class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        comb = []

        def helper(i):
            if len(comb) == k:
                res.append(comb[:])
                return 
            for j in range(i,n + 1):
                comb.append(j)
                helper(j + 1)
                comb.pop()
        helper(1)
        return res