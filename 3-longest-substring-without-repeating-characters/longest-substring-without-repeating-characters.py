class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        a = set()
        left = 0
        ans = 0
        for right in range(len(s)):
            if s[right] in a:
                while s[right] in a:
                    a.remove(s[left])
                    left += 1
            a.add(s[right])
            ans = max(ans,right - left + 1)
        return ans