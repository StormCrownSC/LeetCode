# Given the head of a linked list, remove the nth node from the end of the list and return its head.
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
                """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        l = 0
        elem = head
        while elem is not None:
            elem = elem.next
            l += 1
            
        if l == 1 and n == 1:
            return None
        elif l == n:
            return head.next
        
        n = l - n - 1
        elem = head
        
        while n > 0:
            elem = elem.next
            n -= 1
            
        if elem.next.next is None:
            elem.next = None
        else:
            temp = elem.next
            elem.next = temp.next
            del temp
            
        return head