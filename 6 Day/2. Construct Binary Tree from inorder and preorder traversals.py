# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder)==0 or len(inorder)==0:
            return None
        root = TreeNode(preorder[0])
        ind = inorder.index(preorder[0])
        inorderleft = inorder[:ind]
        inorderright = inorder[ind+1:]
        preorderleft = preorder[1:ind+1]
        preorderright = preorder[ind+1:]
        #print(inorderleft,inorderright,preorderleft,preorderright)
        root.left = self.buildTree(preorderleft,inorderleft)
        root.right = self.buildTree(preorderright,inorderright)
        return root
"""
TC - O(N)
SC - O(N)
"""
