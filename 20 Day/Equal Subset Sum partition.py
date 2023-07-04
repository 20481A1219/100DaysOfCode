class Solution:
    def canPartition(self, arr: List[int]) -> bool:
        target=sum(arr)
        n=len(arr)
        s=target//2
        
        if target%2==1:
            return False
        
        dp=[[False]*(s+1) for i in range(n)]

        for i in range(n):
            dp[i][0]=True
        
        if arr[0]<=s:
            dp[0][arr[0]]=True
        
        for i in range(1,n):
            for j in range(1,s+1):
                not_take=dp[i-1][j]
                take=False
                if j >=arr[i]:
                    take=dp[i-1][j-arr[i]]
                
                dp[i][j]=not_take or take
        
        return dp[n-1][s]
