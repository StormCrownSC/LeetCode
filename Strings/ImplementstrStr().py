class Solution(object):
    def strStr(self, haystack, needle):
        length = len(needle)
        for index in range(len(haystack)):
            if haystack[index:index + length] == needle:
                return index
        return -1
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

if __name__ == "__main__":
	F = Solution()
	print(F.strStr("hello", "ll"))
	print(F.strStr("sadbutsad"), "sad")
	print(F.strStr("leetcode", "leeto"))

"""       
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
"""