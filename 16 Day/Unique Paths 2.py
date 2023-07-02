class Solution:
    def uniquePathsWithObstacles(self, Grid: List[List[int]]) -> int:
        r=len(Grid)
        c=len(Grid[0])

        dp=[[0]*c for i in range(r)]

        for i in range(r):
            if Grid[i][0]!=1:
                dp[i][0]=1
            else:
                break
        
        for i in range(c):
            if Grid[0][i]!=1:
                dp[0][i]=1
            else:
                break
            
        for i in range(1,r):
            for j in range(1,c):
                if Grid[i][j]!=1:
                    dp[i][j]=dp[i-1][j]+dp[i][j-1]
        
        return dp[-1][-1]
