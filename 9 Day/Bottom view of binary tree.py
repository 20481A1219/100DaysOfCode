class Solution:
    def bottomView(self, root):
        # code here
        if not root:
            return []
        q=deque([(root,0)])
        d=defaultdict(int)
        while q:
            k,l=q.popleft()
            d[l]=k.data
            if(k.left):
                q.append((k.left,l-1))
            if(k.right):
                q.append((k.right,l+1))
        ans=[]
        for i in sorted(d.keys()):
            ans.append(d[i])
        return ans

# Take verticals line in each node 
# And for every vertical line take only the last node of it and add it to the map.

  """
  TC-O(N)
  SC-O(N)+O(N)
  """
