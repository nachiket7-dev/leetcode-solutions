class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        b = nums.count(val)
        for i in range(b):
            nums.remove(val)
        return len(nums)