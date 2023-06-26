# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q=deque([(root,0,0)])
        d=defaultdict(dict)

        while q:
            for i in range(len(q)):

                k,line,level = q.popleft()

                if level not in d[line]:
                    d[line][level]=[k.val]
                else:
                    d[line][level].append(k.val)

                if k.left:
                    q.append((k.left,line-1,level+1))
                if k.right:
                    q.append((k.right,line+1,level+1))
        #print(d)
        ans=[]

        for i in sorted(d.keys()):
            e=[]
            for j in d[i]:
                d[i][j].sort()
                e.extend(d[i][j])
            ans.append(e)
                
        return ans 
"""
Maintain the level,line, and element in the queue and them to the dictionary by keeping line numbers as keys 
and each element in the main dictionary is a dictionary with level as keys
And here the main thing we should consider we have to sort the elements when they are having the same line, level numbers
TC-O(NLogN) just iterating throught the tree and also sorting the dictionary
SC-O(N) for queue + O(N) for dictionaryc
"""
