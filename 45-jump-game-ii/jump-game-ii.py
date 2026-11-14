class Solution:
    def jump(self, nums: list[int]) -> int:
        n = len(nums)
        jumps = 0
        farthest = 0
        currEnd = 0
        for i in range(n - 1):
            farthest = max(farthest,i + nums[i])
            if i == currEnd:
                jumps += 1
                currEnd = farthest
        return jumps
            