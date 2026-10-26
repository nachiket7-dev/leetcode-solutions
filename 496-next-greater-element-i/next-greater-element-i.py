class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ans = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    a = -1
                    for k in range(j + 1,len(nums2)):
                        if nums2[k] > nums2[j]:
                            a = nums2[k]
                            break
                    ans.append(a)
        return ans
