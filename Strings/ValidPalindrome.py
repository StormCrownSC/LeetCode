class Solution(object):
    def isPalindrome(self, s):
        if 1 <= len(s) <= 2 * 10**5:
            s = "".join(elem for elem in s if elem.isalnum()).lower()
            return s[:len(s)//2] == s[len(s)//2:][::-1] if len(s) % 2 == 0 else s[:len(s)//2] == s[len(s)//2 + 1:][::-1]
        return False


if __name__ == "__main__":
    First = Solution()
    s1 = "A man, a plan, a canal: Panama"
    s2 = "race a car"
    s3 = " "
    s4 = "aa"
    s5 = "0P"
    print(First.isPalindrome(s1))
    print(First.isPalindrome(s2))
    print(First.isPalindrome(s3))
    print(First.isPalindrome(s4))
    print(First.isPalindrome(s5))

"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
"""