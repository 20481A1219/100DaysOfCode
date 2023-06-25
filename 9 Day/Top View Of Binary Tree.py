import collections
class Solution:
    #Function to return a list of nodes visible from the top view 
    #from left to right in Binary Tree.
    def topView(self,root):
        # code here
        if not root:
            return []
        q=collections.deque([(root,0)])
        d=collections.defaultdict(int)
        while q:
            k,l=q.popleft()
            if l not in d:
                d[l]=k.data
            if(k.left):
                q.append((k.left,l-1))
            if(k.right):
                q.append((k.right,l+1))
        ans=[]
        for i in sorted(d.keys()):
            ans.append(d[i])
        return ans

# take only the first element of each vertical line
