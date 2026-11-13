class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        ans = ''
        while i >= 0 or j >= 0:
            x,y = 0,0
            if i >= 0:
                x = int(a[i])
            if j >= 0:
                y = int(b[j])
            total = x + y + carry
            carry = total // 2
            ans += str(total % 2)
            i -= 1
            j -= 1
        if carry != 0:
            ans += str(carry)
        ans = ans[::-1]
        return ans