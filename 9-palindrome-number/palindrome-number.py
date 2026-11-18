class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = str(x)
        z = y[::-1]
        return (y == z)