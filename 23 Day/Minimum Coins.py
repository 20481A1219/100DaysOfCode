class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n=len(coins)
        dp=[[0]*(amount+1) for i in range(n)]

        for i in range(amount+1):
            if i%coins[0]==0:
                dp[0][i]=i//coins[0]
            else:
                dp[0][i]=10e9
            
        for i in range(1,n):
            for j in range(amount+1):

                not_take=dp[i-1][j]
                take=10e9
                if j>=coins[i]:
                    take=1+dp[i][j-coins[i]]
                
                dp[i][j]=min(not_take,take)

        if dp[-1][-1]>=10e9:
            return -1
        else:
            return dp[-1][-1]
