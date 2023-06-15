# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
Simple Breadth-FIRST SEARCH Approach
"""
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            l=[]
            return l 
        ans=[[root.val]]
        q=deque([root])
        while q:
            k=[]
            for i in range(len(q)):
                curr=q.popleft()
                if curr.left:
                    q.append(curr.left)
                    k.append(curr.left.val)
                if curr.right:
                    q.append(curr.right)
                    k.append(curr.right.val)
            if len(k)>0:        
                ans.append(k)
        return ans
# TC - O(N) for iterating through every node
# SC - O(N) 
