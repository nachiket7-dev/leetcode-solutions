class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        n = len(candidates)
        ans = []
        def helper(start,rem,path):
            if rem == 0:
                ans.append(path[:])
                return
            if start >= n or rem < 0:
                return
            for i in range(start, n):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                path.append(candidates[i])
                helper(i + 1,rem - candidates[i],path)
                path.pop()
        helper(0,target,[])
        return ans