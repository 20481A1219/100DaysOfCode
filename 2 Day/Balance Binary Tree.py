# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balance=True
        self.height(root)
        return self.balance
    def height(self,root):
        if not root:
            return 0
        l=self.height(root.left)
        r=self.height(root.right)
        #print(root.val,abs(left-right))
        if(abs(l-r)>1):
            self.balance=False
        return max(l,r)+1

# As we are finding the left and right height for every node
# We need to just get their absolute difference and then if it is >1 then it is false
# We can also further optimise it.

#TC - O(N)
#SC - O(N)
