class Solution:
    def reverse(self, x: int) -> int:
        a = 0
        if x < 0:
            a = str(x)[1:]
            b = int(a[::-1]) * -1
        else:
            a = str(x)[::-1]
            b = int(a)
        if b >= 2 ** 31 or b < (-2) ** 31:
            return 0
        return b