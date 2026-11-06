class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # if n == 0:
        #     return 1
        # if n > 0:
        #     return x * self.myPow(x,n - 1)
        # else:
        #     return (1 / x) * self.myPow(x,n + 1)
        return x ** n