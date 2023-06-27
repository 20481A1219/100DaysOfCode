# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        l=[]
        ans=[]
        def find(root,l,ans):
            if not root:
                return
            l.append(str(root.val))
            if not root.left and not root.right:
                k="->".join(l)
                ans.append(k)
            find(root.left,l,ans)
            find(root.right,l,ans)
            l.pop()
        find(root,l,ans)
        return ans
