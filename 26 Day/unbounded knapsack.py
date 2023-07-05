#User function Template for python3

class Solution:
    def knapSack(self, n, W, val, wt):
        # code here
        
        dp=[[0]*(W+1) for i in range(n)]
        
        
        for i in range(W+1):
            dp[0][i]=(i//wt[0])*val[0]
            
        for i in range(1,n):
            for j in range(W+1):
                
                not_take=dp[i-1][j]
                take=-10**9
                if j>=wt[i]:
                    take=dp[i][j-wt[i]]+val[i]
                    
                dp[i][j]=max(not_take,take)
                
        return dp[-1][-1]
