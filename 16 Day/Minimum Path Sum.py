class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        r=len(grid)
        c=len(grid[0])

        dp=[[-1]*c for i in range(r)]

        for i in range(r):
            for j in range(c):
                if i==0 and j==0:
                    dp[i][j]=grid[0][0]
                else:
                    if i==0:
                        dp[i][j]=dp[i][j-1]+grid[i][j]
                    elif j==0:
                        dp[i][j]=dp[i-1][j]+grid[i][j]
                    else:
                        dp[i][j]=min(dp[i-1][j],dp[i][j-1])+grid[i][j]

        return dp[-1][-1]
