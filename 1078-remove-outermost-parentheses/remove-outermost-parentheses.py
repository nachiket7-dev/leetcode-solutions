class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = ''
        count = 0
        for i in s:
            if i == '(':
                if count > 0:
                    ans += i
                count += 1
            else:
                count -= 1
                if count > 0:
                    ans += i
        return ans
