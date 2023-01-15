# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.find(root, 0)
        
    def find(self, root, count):
        if root != None:
            depth1 = self.find(root.left, count + 1)
            depth2 = self.find(root.right, count + 1)
            return depth1 if depth1 > depth2 else depth2
        return count


"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
"""