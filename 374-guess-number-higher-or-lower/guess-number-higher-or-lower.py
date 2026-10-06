# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        st = 1
        end = n
        while st <= end:
            mid = (st + end) // 2
            res = guess(mid)
            if res == 1:
                st = mid + 1
            elif res == -1:
                end = mid - 1
            else:
                return mid

