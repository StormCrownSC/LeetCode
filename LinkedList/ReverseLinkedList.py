class Solution:
    def reverseList(self, list):
        return self.reverse(list)
    
    def longestPalindrome(self, s: str) -> str:
        pass
    
    def reverse(self, head):
        last = None
        val = head
        while val:
            tmp = val.next
            val.next = last
            last = val
            val = tmp
        return last

"""
Given the head of a singly linked list, reverse the list, and return the reversed list.
"""