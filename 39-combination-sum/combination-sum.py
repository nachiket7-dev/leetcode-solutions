class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        n = len(candidates)
        ans = []
        def helper(i,rem,path):
            if rem == 0:
                ans.append(path[:])
                return
            if i >= n or rem < 0:
                return
            path.append(candidates[i])
            helper(i,rem - candidates[i],path)
            path.pop()
            helper(i + 1,rem,path)
        helper(0,target,[])
        return ans
            