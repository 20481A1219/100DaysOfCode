# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
Recursive DFS
"""
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left=self.maxDepth(root.left)
        right=self.maxDepth(root.right)

        return max(left,right)+1

# Here we need to traverse through the tree
# Then find the height of the max(left and right) subtree for each node and add 1 to it
# TC: O(N) for traversing through the nodes 
# SC: O(N) for stack space
 
"""
Iterative BFS
"""
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        level=0
        q=deque([root])
        while q:
            for i in range(len(q)):
                node=q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level+=1
        return level
# Just need to find the no of levels and return it.
# TC: O(N) for visiting all nodes
# SC: O(N) for queue 

"""
Iterative DFS
"""
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [[root, 1]]
        res = 0
        while stack:
            node, depth = stack.pop()
            if node:
                res = max(res, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        return res
# Just need to go level by level and changing the depth values and storing the max depth till now in res
# At the end return result
# Same time and space complexity O(N)
