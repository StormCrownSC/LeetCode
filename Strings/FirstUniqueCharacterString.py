class Solution(object):
    def firstUniqChar(s):
        letters='abcdefghijklmnopqrstuvwxyz'
        data = [s.index(elem) for elem in letters if s.count(elem) == 1]
        return min(data) if len(data) > 0 else -1


if __name__ == "__main__":
    print(Solution.firstUniqChar("leetcode"))
    print(Solution.firstUniqChar("loveleetcode"))
    print(Solution.firstUniqChar("aabb"))

"""
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
"""