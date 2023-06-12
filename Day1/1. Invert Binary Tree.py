# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
Depth-First Search Approach
"""
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        self.invertTree(root.left)
        self.invertTree(root.right)
        root.left,root.right=root.right,root.left
        return root

# Here just we need to traverse the tree
# And then swap the left and right parts of each node
# And then finally return that node.
# Time Complexity: O(N), Visiting all the nodes of the tree of size N
# Auxiliary Space: O(N), For function call stack space


"""
Breadth-First Search Approach
"""
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        q=collections.deque([root])
        while (len(q))>0:
            curr=q.popleft()
            curr.left,curr.right=curr.right,curr.left
            if(curr.left):
                q.append(curr.left)
            if(curr.right):
                q.append(curr.right)
        return root
# Here just we need to traverse the tree and store the nodes at each level, levelwise.
# And then swap the left and right parts of each node
# And then finally return that node.
# Time Complexity: O(N), Visiting all the nodes of the tree of size N
# Auxiliary Space: O(N), Using queue to store the nodes of the tree
