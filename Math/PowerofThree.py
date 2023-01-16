class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return self.check(n)
        
    def check(self, n):
        if n != 0 and n % 3 == 0:
            n = self.check(n//3)
        if n == 1 or n == True:
            return True
        return False

"""
Given an integer n, return true if it is a power of three. Otherwise, return false.

An integer n is a power of three, if there exists an integer x such that n == 3x.
"""