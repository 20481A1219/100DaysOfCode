class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        n=len(coins)
        dp=[[0]*(amount+1) for i in range(n)]

        for i in range(amount+1):
            if i%coins[0]==0:
                dp[0][i]=1

        for i in range(1,n):
            for j in range(amount+1):

                not_take=dp[i-1][j]
                take=0
                if j>=coins[i]:
                    take=dp[i][j-coins[i]]
                
                #print("take",take,"nottake",not_take)
                dp[i][j]=not_take+take
        #print(dp)
        return dp[-1][-1]
