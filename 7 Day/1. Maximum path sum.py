"""
Code with Alisha: https://www.youtube.com/watch?v=JBYs5J4skZE
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans=-10e9
        def find(root):
            if not root:
                return 0
            left=find(root.left)
            right=find(root.right)
            stpath=max(root.val,max(root.val+left,root.val+right))     # root.val  or  root.val+left  or root.val+right   we should take max of it
            curvpath=root.val+left+right                               # root.val+left+right  and this also
            self.ans=max(self.ans,max(stpath,curvpath))                # and update the ans with either of them
            return stpath
        find(root)
        return self.ans
"""
TC - O(N)
SC - O(N)
"""
