# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
Recursive Approach
"""
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val!=q.val:
            return False    
        left=self.isSameTree(p.left,q.left)
        right=self.isSameTree(p.right,q.right)
        return left and right
# Recursive iterate through the array
# Find out the find the value present in the both nodes of p and q same or not. If not then return False.
# TC - O(N)
# SC - O(N)
