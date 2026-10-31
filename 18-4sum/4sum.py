class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        for i in range(len(nums) - 3):
            if i >= 1:
                if nums[i] == nums[i - 1]:
                    continue
            for j in range(i + 1,len(nums) - 2):
                if j >= i + 2:
                    if nums[j] == nums[j - 1]:
                        continue
                left = j + 1
                right = len(nums) - 1
                while left < right:
                    a = nums[i] + nums[j] + nums[left] + nums[right]
                    if a == target:
                        res.append([nums[i],nums[j],nums[left],nums[right]])
                        left += 1
                        right -= 1
                        if left >= right:
                            break
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        if right < len(nums) - 1:
                            while right > left and nums[right] == nums[right + 1]:
                                right -= 1
                    elif a < target:
                        left += 1
                    else:
                        right -= 1
        return res