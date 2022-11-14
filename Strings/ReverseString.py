"""
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.
"""
class Solution(object):
	def reverseString(self, s):
		return s.reverse()


if __name__ == "__main__":
	First = Solution()
	s = ["h", "e", "l", "l", "o"]
	print(str(s) + " = " + str(First.reverseString(s)))

