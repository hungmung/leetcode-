"""
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        copy = x
        mirror = 0
        while x > 0:
            r = x%10
            mirror = mirror*10 + r
            x = x//10
        return mirror==copy
