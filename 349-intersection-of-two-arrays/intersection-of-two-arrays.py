class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort()
        nums2.sort()
        ans = []
        for i in nums1:
            for j in nums2:
                if i == j:
                    if i not in ans:
                        ans.append(i)
        return ans