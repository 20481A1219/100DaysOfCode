# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
DFS Recursive
TC - O(N)
SC - O(N)
"""
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.l=[]
        def inorder(root):
            if root:
                inorder(root.left)
                self.l.append(root.val)
                inorder(root.right)
        inorder(root)
        #print(self.l)
        return self.l[k-1]

"""
DFS iterative using stack
"""
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack=[]
        curr=root
        while stack or curr:
            while curr:
                stack.append(curr)
                curr=curr.left
            curr=stack.pop()
            k=k-1
            if k==0:
                return curr.val
            curr=curr.right
# TC - O(N)
# SC - O(H) only takes one path elements in it. so max it is height of the tree only

