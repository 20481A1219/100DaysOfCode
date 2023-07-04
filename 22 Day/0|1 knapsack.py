class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
       
        # code here
        dp=[[0]*(W+1) for i in range(n)]
        
        for i in range(wt[0],W+1):
            dp[0][i]=val[0]
            
        for i in range(1,n):
            for j in range(W+1):
                
                not_take=dp[i-1][j]
                take=0
                if j>=wt[i]:
                    take=dp[i-1][j-wt[i]]+val[i]
                
                dp[i][j]=max(not_take,take)
        
        return dp[n-1][W]
