class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:  
        r=len(matrix)
        c=len(matrix[0])

        dp=[[-1]*c for i in range(r)]

        for i in range(r):
            for j in range(c):
                if i==0:
                    dp[i][j]=matrix[i][j]
                else:
                    if j==0:
                        dp[i][j]=min(dp[i-1][j],dp[i-1][j+1])+matrix[i][j]
                    elif j==c-1:
                        dp[i][j]=min(dp[i-1][j],dp[i-1][j-1])+matrix[i][j]
                    else:
                        dp[i][j]=min(dp[i-1][j],dp[i-1][j+1],dp[i-1][j-1])+matrix[i][j]
        return min(dp[-1])
