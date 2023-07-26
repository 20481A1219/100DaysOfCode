class Solution:

    def findMinDiff(self, A,n,m):

        # code here
        A.sort()
        
        mi=10**9
        
        for i in range(n-m+1):
            mi=min(A[i+m-1]-A[i],mi)
        
        return mi
