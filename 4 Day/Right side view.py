# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q=deque([root])
        ans=[]
        while q:
            l=len(q)
            for i in range(l):
                curr=q.popleft()
                if i==l-1:
                    ans.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
        return ans
# Just find out the right most node in every level 
# we can easily find it out using level order traversal
# TC - O(N) 
# SC - O(N)
