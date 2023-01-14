# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        
        while True:
            if list1.val > list2.val:
                temp = list1
                list1 = list2
                list2 = temp
            list1 = self.addNode(list1, list2.val)
            list2 = list2.next
            if list2 == None:
                return list1
        
    def addNode(self, list1, elem):
        return self.findNode(list1, elem)

    def findNode(self, list1, elem):
        head = list1
        while list1 != None:
            if list1.next == None or self.checkNextNode(elem, list1.next.val):
                node = ListNode(elem, list1.next)
                list1.next = node
                return head
            list1 = list1.next
        return head
        
    def checkNextNode(self, first, second):
        return first <= second

"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""