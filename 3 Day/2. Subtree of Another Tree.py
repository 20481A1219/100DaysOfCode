# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        if self.sameTree(root,subRoot):
            return True
        left=self.isSubtree(root.left,subRoot)
        right=self.isSubtree(root.right,subRoot)
        return left or right
    def sameTree(self,root,subRoot):
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        if root.val!=subRoot.val:
            return False
        left=self.sameTree(root.left,subRoot.left)
        right=self.sameTree(root.right,subRoot.right)
        return left and right

# Iterative through node and find out if from that node onwards whether it forms the subtree given
# we can use sameTree function as helper function
# if big tree contains N nodes and small tree contains M nodes then 
# TC - O(M*N)
# SC - O(N) max stack size is the small tree no of nodes only
