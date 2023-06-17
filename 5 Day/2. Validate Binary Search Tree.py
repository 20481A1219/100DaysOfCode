# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def find(root,left,right):
            if not root:
                return True
            if not (left<root.val and right>root.val):
                return False
            l=find(root.left,left,root.val)
            r=find(root.right,root.val,right)
            return l and r
        return find(root,-10e9,10e9)
# Just need to check whether each node is in correct range or not
# left node = range( minval , root.val )
# right node = range( root.val , maxval)
# TC - O(N)
# SC - O(N)
