"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
"""
class Solution(object):
	def reverse(self, x):
		if -2**31 > x or x > 2**31 - 1:
			return 0
		data = str(abs(x))
		if x < 0:
			data += "-"
		return int(data[::-1]) if -2**31 <= int(data[::-1]) <= 2**31 - 1 else 0


if __name__ == "__main__":
	a = 123
	b = -256
	c = -210
	F = Solution()
	print(str(a) + " = " + str(F.reverse(a)))
	print(str(b) + " = " + str(F.reverse(b)))
	print(str(c) + " = " + str(F.reverse(c)))
	

