# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
Breadth First Search Approach
"""
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        q=deque()
        q.append([root,root.val])
        count=0
        while q:
            node,m=q.popleft()
            if node.val>=m:
                m=node.val
                count+=1
            if node.left:
                q.append([node.left,m])
            if node.right:
                q.append([node.right,m])
        return count
# if node.val is greater than the max val we seen till now then we can update that max val to node val and increase the count by 1
# TC - O(N)
# SC - O(N)

"""
Depth First Search Approach
"""
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        def find(root,m):
            if not root:
                return 0
            if root.val >= m:
                return 1 + find(root.left,max(root.val,m)) + find(root.right,max(root.val,m))
            else:
                return find(root.left,m) + find(root.right,m)
        return find(root,root.val)
# count=1+left+right if node.val is greater than max value
# else just left+right
# Same TC and SC
