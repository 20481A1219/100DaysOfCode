class Solution:
    def countPartitions(self, n, d, arr):
        # Code here
        s=sum(arr)
        target=(s-d)//2
        
        if s-d<0 or (s-d)%2==1:
            return 0
        
        dp=[[0]*(target+1) for i in range(n)]
        
        mod=10**9+7
        
        for i in range(n):
            dp[i][0]=1
        
        if arr[0]<=target:
            dp[0][arr[0]]+=1
            
        for i in range(1,n):
            for j in range(target+1):
                
                not_take=dp[i-1][j]
                
                take=0
                if j>=arr[i]:
                    take=dp[i-1][j-arr[i]]
                
                dp[i][j]=(not_take+take)%mod
        
        return dp[-1][-1]%mod
