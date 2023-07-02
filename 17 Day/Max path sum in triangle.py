class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        r=len(triangle)
        
        dp=[[-1]*r for i in range(r)]

        dp[0][0]=triangle[0][0]
        c=2
        for i in range(1,r):
            for j in range(c):
                if j==0:
                    dp[i][j]=dp[i-1][j]+triangle[i][j]
                elif j==c-1:
                    dp[i][j]=dp[i-1][j-1]+triangle[i][j]
                else:
                    dp[i][j]=min(dp[i-1][j],dp[i-1][j-1])+triangle[i][j]
            c=c+1
        
        return min(dp[-1])
