class Solution(object):
    def isAnagram(self, s, t):
        if 1 <= len(s) <= 5 * 10**4 and 1 <= len(t) <= 5 * 10**4:
            letters='abcdefghijklmnopqrstuvwxyz'
            data = [s.index(elem) for elem in letters if s.count(elem) == 1]
            data_1 = {elem: s.count(elem) for elem in letters if s.count(elem) != 0}
            data_2 = {elem: t.count(elem) for elem in letters if t.count(elem) != 0}
            if data_1.keys() != data_2.keys():
                return False
            for key, value in data_1.items():
                if data_2[key] != value:
                    return False
            return True
        return False


if __name__ == "__main__":
    First = Solution()
    # s = "anagram"
    # t = "nagaram"
    s = "a"
    t = "ab"
    print(First.isAnagram(s, t))
