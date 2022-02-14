# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
# 
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

class Solution:
    def reverse(self, x: int) -> int:
        rev = "{}".format(abs(x))
        rev = rev[::-1]
        irev = int(rev)
        if x<0: irev *= -1
        if irev > (2**31-1) or irev < -1*2**31: return 0
        return irev
